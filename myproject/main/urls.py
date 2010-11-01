from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('myproject.main.views',
    url(r'about/$', 'about', name='about'),
    url(r'aboutsite/$', 'aboutsite', name='aboutsite'),
    url(r'past_meetings/(?P<pagenum>\d+)/$',
         'past_meetings',
         name="past-meetings-page"),
    url(r'past_meetings/$', 'past_meetings', name="past-meetings"),
    url(r'contactus/$', 'contactus', name="contactus"),
    url(r'^$', 'index', name='index'),
)
