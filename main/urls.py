from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('opag.main.views',
    url(r'membership/$', 'membership'),
    url(r'aboutsite/$', 'aboutsite'),
    url(r'past_meetings/(?P<pagenum>\d+)/$',
         'past_meetings',
         name="past-meetings-page"),
    url(r'past_meetings/$', 'past_meetings', name="past-meetings"),
    url(r'contactus/$', 'contactus', name="contactus"),
    url(r'^$', 'index'),
)
