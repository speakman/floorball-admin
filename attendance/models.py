from django.db import models
from django.forms import ModelForm
from datetime import date
from math import floor

class Participant(models.Model):
    name = models.CharField(max_length=60)
    nin = models.CharField(max_length=11,blank=True)
    phone = models.CharField(max_length=30,blank=True)
    email = models.EmailField(blank=True)
    has_payed = models.BooleanField()

    def birthdate(self):
        if len(self.nin) >= 6:
            return date(int("19"+self.nin[0:2]),
                        int(self.nin[2:4]),
                        int(self.nin[4:6]))

    def age(self):
        diff = date.today() - self.birthdate()
        return int(floor(diff.days / 365.25))

    @models.permalink
    def get_absolute_url(self):
	return ("view_participant", [str(self.id)])

    def __unicode__(self):
        return self.name


class Gathering(models.Model):
    date = models.DateField()
    participants = models.ManyToManyField(Participant,blank=True)

    def __unicode__(self):
        return self.date.strftime("%Y-%m-%d")


class ParticipantForm(ModelForm):
    class Meta:
        model = Participant
