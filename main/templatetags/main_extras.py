from django import template
from django.shortcuts import get_object_or_404
from opag.main.models import NewsArticle

register = template.Library()

@register.inclusion_tag('main/single_article.html')
def display_article(id, bglist, bgindex=0, limit=0):
    """This inclusion tag renders a template to display an article, with an
    optional argument to limit the content to a number of words."""
    bglist = bglist.split(',')
    bg = bglist[bgindex % len(bglist)]
    id = int(id)
    article = get_object_or_404(NewsArticle, id=id)

    return {
        'article': article,
        'limit': limit,
        'bg': bg
        }
