from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'attendance.views.home', name='home'),

    url(r'^toggle_attendance/$', 'attendance.views.toggle_attendance', name="toggle_attendance"),

    url(r'^participants/(\d+)/$', 'attendance.views.participant', name="view_participant"),
    url(r'^participants/new/$', 'attendance.views.participant', name="new_participant"),
    url(r'^gatherings/new/$', 'attendance.views.gathering', name="new_gathering"),

    #url(r'^floorball/', include('floorball.foo.urls')),

    # Uncomment the admin/doc< line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
     {'document_root': settings.MEDIA_ROOT}),

)
