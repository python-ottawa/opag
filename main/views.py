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

published_articles = NewsArticle.objects.all().filter(approved=True).order_by('-submitted_date')
top3_articles = published_articles[:3]
top10_articles = published_articles[:10]

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
    return render_to_response('main/index.html',
                              { 'articles': published_articles,
                                'top3_articles': top3_articles,
                                'top10_articles': top10_articles,
                                'bctrail': bctrail },
                                context_instance=RequestContext(request))

def contactus(request):
    "The contact us page."
    bctrail = make_bctrail(['Home', '/', 'Contact us'])
    return render_to_response('main/contactus.html',
                              { 'articles': published_articles,
                                'top3_articles': top3_articles,
                                'top10_articles': top10_articles,
                                'bctrail': bctrail },
                                context_instance=RequestContext(request))

def membership(request):
    "The membership page."
    bctrail = make_bctrail(['Home', '/', 'Membership instructions'])
    return render_to_response('main/membership.html',
                              { 'top10_articles': top10_articles,
                                'bctrail': bctrail },
                                context_instance=RequestContext(request))

def past_meetings(request):
    "The archived meetings page."
    bctrail = make_bctrail(['Home', '/',
                            'Meetings', '/meetings/',
                            'Past meetings'])
    meetings = Meeting.objects.all().filter(date__lt=date.today()).order_by('-date')
    meetings = __preprocess_meetings(meetings)
    return render_to_response('main/past_meetings.html',
                              { 'top10_articles': top10_articles,
                                'meetings': meetings,
                                'bctrail': bctrail },
                                context_instance=RequestContext(request))

def meetings(request):
    "The meetings page."
    bctrail = make_bctrail(['Home', '/', 'Meeting information'])
    meetings = Meeting.objects.all().filter(date__gte=date.today()).order_by('date')
    meetings = __preprocess_meetings(meetings)
    return render_to_response('main/meetings.html',
                              { 'top10_articles': top10_articles,
                                'meetings': meetings,
                                'bctrail': bctrail },
                                context_instance=RequestContext(request))

def aboutsite(request):
    "The about site page."
    bctrail = make_bctrail(['Home', '/', 'About site'])
    return render_to_response('main/aboutsite.html',
                              { 'top10_articles': top10_articles,
                                'bctrail': bctrail },
                                context_instance=RequestContext(request))

def articles(request):
    "The articles page."
    bctrail = make_bctrail(['Home', '/', 'Articles'])
    articles = Article.objects.all()
    return render_to_response('main/articles.html',
                              { 'top10_articles': top10_articles,
                                'articles': articles,
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
                              { 'top10_articles': top10_articles,
                                'article': article,
                                'bctrail': bctrail },
                                context_instance=RequestContext(request))

def news_all(request, page=1):
    """This function displays the interface to all news in the database."""
    page = int(page)
    bctrail = make_bctrail(['Home', '/', 'All news'])
    paginator = OpagPaginator(request, published_articles, page, page_size=10)
    page = paginator.get_page(page)
    return render_to_response('main/news_all.html',
        RequestContext(request, {
            'top10_articles': top10_articles,
            'paginator': paginator,
            'bctrail': bctrail,
            'page': page
            }))

def news_article(request, id):
    """This function displays the interface to an individual news article."""
    try:
        myid = int(id)
        article = NewsArticle.objects.filter(id=myid)[0]
        if not article:
            raise ValueError, "failed to fetch article %d from db" % myid
    except Exception, err:
        raise Http404, "article id of %s does not exist" % id
    bctrail = make_bctrail(['Home', '/', 'All news', '/news/', 'Article %d' % myid])
    return render_to_response('main/news_article.html',
                              { 'top10_articles': top10_articles,
                                'article':  article,
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
