from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404
from django.core.paginator import Paginator
from myproject.main.models import Meeting, Notice
from myproject.lib.paginator import OpagPaginator
from datetime import date
from time import time

def index(request):
    "The home page."
    meetings = Meeting.objects.all().filter(
        date__gte=date.today()).order_by('date')
    notices = Notice.objects.all().order_by('submitted_date')
    return render_to_response('main/index.html',
        RequestContext(request, {
            'meetings': meetings,
            'notices': notices,
            }))

def contactus(request):
    "The contact us page."
    return render_to_response('main/contactus.html',
        RequestContext(request, {
            }))

def about(request):
    "The membership page."
    return render_to_response('main/about.html',
        RequestContext(request, {
            }))

def past_meetings(request, pagenum=1):
    "The archived meetings page."
    nperpage = 2
    meetings = Meeting.objects.all().filter(date__lt=date.today()).order_by('-date')
    paginator = Paginator(meetings, nperpage)
    page = paginator.page(pagenum)
    page.pagenum = pagenum
    return render_to_response('main/past_meetings.html',
        RequestContext(request, {
            'meetings': page.object_list,
            'page': page,
            }))

def aboutsite(request):
    "The about site page."
    return render_to_response('main/aboutsite.html',
        RequestContext(request, {
            }))

def notfound(request):
    "A 404 handler."
    res = render_to_response('404.html',
        RequestContext(request, {
            }))
    res.status_code = 404
    return res

def servererror(request):
    "A handler for displaying a 'not yet implemented' interface."
    res = render_to_response('500.html',
        RequestContext(request, {
            }))
    res.status_code = 500
    return res
