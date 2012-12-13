from django import template
from django.core.urlresolvers import reverse

register = template.Library()

rootpath = '/'

@register.tag
def init_rootpath(parser, token):
    """This function returns a RootPathNode object, initialized with the path
    passed in via the token."""
    return RootPathNode()

class RootPathNode(template.Node):
    """This class populates the context with a variable called 'rootpath' that
    can be used to prefix relative urls so that they work if the install
    location changes. The root path will need to be changed in this module for
    that to work."""

    def render(self, context):
        context['rootpath'] = rootpath
        return ''


@register.inclusion_tag('lmenu.html')
def left_menu():
    "This inclusion tag sets up the data for the left menu."
    club_info = [
        {
            'title': 'About the group',
            'link': reverse('about')
        },
        {
            'title': 'About the website',
            'link': reverse('aboutsite')
        },
        {
            'title': 'Financials',
            'link': rootpath + 'financials/' # FIXME: can I use reverse with
        },                                   # with a flatpage? What about
        {                                    # the bctrail?
            'title': 'Contact Us',
            'link': reverse('contactus')
        }
    ]

    menu = [
        {
            'title': 'Club Information',
            'image': 'club_information.png',
            'data': club_info
        }
    ]
    return { 'menu': menu }

@register.inclusion_tag('rmenu.html', takes_context=True)
def right_menu(context):
    "This inclusion tag sets up the data for the right menu."
    quick_links = [
        {
            'title': 'The Python Homepage',
            'link': 'http://www.python.org/'
        },
        {
            'title': 'Digital Torque Consulting Inc.',
            'link': 'http://digitaltorque.ca/'
        },
        {
            'title': "Michael Soulier's Blog",
            'link': 'http://www.but-i-digress.ca/'
        },
        {
            'title': "Ian Ward's Homepage",
            'link': 'http://excess.org/'
        },
        {
            'title': "Tyler Kennedy's Blog",
            'link': 'http://w.tkte.ch'
        }
    ]
    return { 'quicklinks': quick_links,
             'rootpath': rootpath }
