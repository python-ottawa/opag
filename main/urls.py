from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'membership/$', 'opag.main.views.membership'),
    (r'^meetings/$', 'opag.main.views.meetings'),
    (r'aboutsite/$', 'opag.main.views.aboutsite'),
    (r'past_meetings/$', 'opag.main.views.past_meetings'),

    (r'articles/$', 'opag.main.views.articles'),
    (r'articles/(?P<id>\d+)/$', 'opag.main.views.view_article'),
    (r'contactus/$', 'opag.main.views.contactus'),

    (r'news/$', 'opag.main.views.news_all'),
    (r'news/page/(?P<page>\d+)/$', 'opag.main.views.news_all'),
    (r'news/article/(?P<id>\d+)/$', 'opag.main.views.news_article'),

    (r'^$', 'opag.main.views.index'),
)
