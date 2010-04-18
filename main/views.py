# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404
from opag.main.models import *
from opag.lib.shared import make_bctrail
from opag.lib.paginator import OpagPaginator
from datetime import date
from time import time

def __preprocess_meetings(meetings):
    """This function takes a list of meeting objects, and iterates over them,
    populating the human_month and human_datetime fields, and returns the
    resulting list."""
    for meeting in meetings:
        meeting.human_month = meeting.date.strftime("%B")
        meeting.human_datetime = meeting.date.strftime("%c")
    return meetings

def index(request):
    "The home page."
    bctrail = 'Home'
    meetings = Meeting.objects.all().filter(
        date__gte=date.today()).order_by('date')
    meetings = __preprocess_meetings(meetings)
    return render_to_response('main/index.html',
        RequestContext(request, {
            'meetings': meetings,
            'bctrail': bctrail }))

def contactus(request):
    "The contact us page."
    bctrail = make_bctrail(['Home', '/', 'Contact us'])
    return render_to_response('main/contactus.html',
                              { 'articles': published_articles,
                                'bctrail': bctrail },
                                context_instance=RequestContext(request))

def membership(request):
    "The membership page."
    bctrail = make_bctrail(['Home', '/', 'Membership instructions'])
    return render_to_response('main/membership.html',
                              { 'bctrail': bctrail },
                                context_instance=RequestContext(request))

def past_meetings(request):
    "The archived meetings page."
    bctrail = make_bctrail(['Home', '/',
                            'Meetings', '/meetings/',
                            'Past meetings'])
    meetings = Meeting.objects.all().filter(date__lt=date.today()).order_by('-date')
    meetings = __preprocess_meetings(meetings)
    return render_to_response('main/past_meetings.html',
                              { 'meetings': meetings,
                                'bctrail': bctrail },
                                context_instance=RequestContext(request))

def meetings(request):
    "The meetings page."
    bctrail = make_bctrail(['Home', '/', 'Meeting information'])
    meetings = Meeting.objects.all().filter(date__gte=date.today()).order_by('date')
    meetings = __preprocess_meetings(meetings)
    return render_to_response('main/meetings.html',
                              { 'meetings': meetings,
                                'bctrail': bctrail },
                                context_instance=RequestContext(request))

def aboutsite(request):
    "The about site page."
    bctrail = make_bctrail(['Home', '/', 'About site'])
    return render_to_response('main/aboutsite.html',
                              { 'bctrail': bctrail },
                                context_instance=RequestContext(request))

def articles(request):
    "The articles page."
    bctrail = make_bctrail(['Home', '/', 'Articles'])
    articles = Article.objects.all()
    return render_to_response('main/articles.html',
                              { 'articles': articles,
                                'bctrail': bctrail },
                                context_instance=RequestContext(request))

def view_article(request, id):
    "The individual article list page."
    id = int(id)
    bctrail = make_bctrail(['Home', '/',
                            'Articles', '/articles/',
                            'Article %d' % id])
    article = get_object_or_404(Article, id=id)
    return render_to_response('main/view_article.html',
                              { 'article': article,
                                'bctrail': bctrail },
                                context_instance=RequestContext(request))

def notfound(request):
    "A 404 handler."
    bctrail = make_bctrail(['Home', '/', 'Page not found'])
    return render_to_response('404.html',
                              { 'bctrail': bctrail,
                                'top10_articles': top10_articles })

def servererror(request):
    "A handler for displaying a 'not yet implemented' interface."
    bctrail = make_bctrail(['Home', '/', 'Server error'])
    return render_to_response('500.html',
                              { 'bctrail': bctrail,
                                'top10_articles': top10_articles })
