from django.contrib import admin
from floorball.attendance.models import Gathering, Participant

class GatheringAdmin(admin.ModelAdmin):
    pass
admin.site.register(Gathering, GatheringAdmin)

class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('name', 'nin', 'phone', 'email', 'has_payed')
admin.site.register(Participant, ParticipantAdmin)
