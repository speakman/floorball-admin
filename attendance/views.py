from django.shortcuts import render
from django.http import *
from django.utils import simplejson
from django.views.decorators.csrf import csrf_exempt
from attendance.models import Participant,Gathering,ParticipantForm
from datetime import date


def home(request):
    participants = Participant.objects.order_by('name')
    gatherings = [{"id": x.id,
                   "date": x.date,
                   "participants": x.participants.all()}
                   for x in
                   Gathering.objects.order_by('-date')[:3]]
    return render(request, "home.html", {"participants": participants,
                                         "gatherings": gatherings,
                                         "today": date.today()})


def participant(request, id=None):
    if id is None:
        participant = Participant()
        header = "New participant"
    else:
        try:
            participant = Participant.objects.get(id=id)
        except Participant.DoesNotExist:
            raise Http404
        header = participant.name

    if request.method == "POST":
        form = ParticipantForm(request.POST)
        if form.is_valid():
            participant.name = form.cleaned_data['name']
            participant.nin = form.cleaned_data['nin']
            participant.phone = form.cleaned_data['phone']
            participant.email = form.cleaned_data['email']
            participant.has_payed = form.cleaned_data['has_payed']
            participant.save()
            return HttpResponseRedirect("/")
    else:
        form = ParticipantForm(instance=participant)

    return render(request, "participant.html", {"header": header,
                                                "form": form})


def gathering(request, id=None):
    try:
        Gathering.objects.get(date=date.today())
        return HttpResponseRedirect("/")
    except:
        pass

    gathering = Gathering()
    gathering.date = date.today()
    gathering.save()

    return HttpResponseRedirect("/")

@csrf_exempt
def toggle_attendance(request):
    if request.method != "POST":
        return HttpResponseBadRequest()

    response = {'attended': None}
    gathering = Gathering.objects.get(id=request.POST.get("gathering"))
    participant = Participant.objects.get(id=request.POST.get("participant"))

    if participant in gathering.participants.all():
        gathering.participants.remove(participant)
        response["attended"] = False
    else:
        gathering.participants.add(participant)
        response["attended"] = True
    gathering.save()

    return HttpResponse(simplejson.dumps(response),
                        mimetype='application/javascript; charset=utf-8')
