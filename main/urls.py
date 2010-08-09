from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'membership/$', 'opag.main.views.membership'),
    (r'aboutsite/$', 'opag.main.views.aboutsite'),
    (r'past_meetings/$', 'opag.main.views.past_meetings'),

    (r'contactus/$', 'opag.main.views.contactus'),

    (r'^$', 'opag.main.views.index'),
)
