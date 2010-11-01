from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404
from django.core.paginator import Paginator
from myproject.main.models import Meeting, Notice
from myproject.lib.shared import make_bctrail
from myproject.lib.paginator import OpagPaginator
from datetime import date
from time import time

def index(request):
    "The home page."
    bctrail = 'Home'
    meetings = Meeting.objects.all().filter(
        date__gte=date.today()).order_by('date')
    notices = Notice.objects.all().order_by('submitted_date')
    return render_to_response('main/index.html',
        RequestContext(request, {
            'meetings': meetings,
            'notices': notices,
            'bctrail': bctrail
            }))

def contactus(request):
    "The contact us page."
    bctrail = make_bctrail(['Home', '/', 'Contact us'])
    return render_to_response('main/contactus.html',
        RequestContext(request, {
            'bctrail': bctrail
            }))

def about(request):
    "The membership page."
    bctrail = make_bctrail(['Home', '/', 'About the group'])
    return render_to_response('main/about.html',
        RequestContext(request, {
            'bctrail': bctrail
            }))

def past_meetings(request, pagenum=1):
    "The archived meetings page."
    nperpage = 2
    bctrail = make_bctrail(['Home', '/',
                            'Past meetings'])
    meetings = Meeting.objects.all().filter(date__lt=date.today()).order_by('-date')
    paginator = Paginator(meetings, nperpage)
    page = paginator.page(pagenum)
    page.pagenum = pagenum
    return render_to_response('main/past_meetings.html',
        RequestContext(request, {
            'meetings': page.object_list,
            'page': page,
            'bctrail': bctrail
            }))

def aboutsite(request):
    "The about site page."
    bctrail = make_bctrail(['Home', '/', 'About the website'])
    return render_to_response('main/aboutsite.html',
        RequestContext(request, {
            'bctrail': bctrail
            }))

def notfound(request):
    "A 404 handler."
    bctrail = make_bctrail(['Home', '/', 'Page not found'])
    return render_to_response('404.html',
        RequestContext(request, {
            'bctrail': bctrail
            }))

def servererror(request):
    "A handler for displaying a 'not yet implemented' interface."
    bctrail = make_bctrail(['Home', '/', 'Server error'])
    return render_to_response('500.html',
        RequestContext(request, {
            'bctrail': bctrail
            }))
