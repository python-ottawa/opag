from django import template
from django.shortcuts import get_object_or_404

register = template.Library()

@register.inclusion_tag('main/meeting.html', takes_context=True)
def render_meeting(context, meeting, short=False):
    """The inclusion tag for rendering a meeting."""
    return {
        'meeting': meeting,
        'short': short
        }
