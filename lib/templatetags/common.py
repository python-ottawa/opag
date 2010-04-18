from django import template

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
            'title': 'Membership Instructions',
            'link': rootpath + 'membership/'
        },
        {
            'title': 'About the Website',
            'link': rootpath + 'aboutsite/'
        }
    ]

    resources = [
        {
            'title': 'OPAG Wiki',
            'link': rootpath + 'wiki/'
        },
        {
            'title': 'Contact Us',
            'link': rootpath + 'contactus/'
        }
    ]

    menu = [
        {
            'title': 'Club Information',
            'image': 'club_information.png',
            'data': club_info
        },
        {
            'title': 'Resources',
            'image': 'resources.png',
            'data': resources
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
            'title': 'Dive Into Python',
            'link': 'http://www.diveintopython.org/'
        },
        {
            'title': 'Python 2.5 quick reference',
            'link': 'http://rgruet.free.fr/PQR25/PQR2.5.html'
        },
        {
            'title': 'ActivePython',
            'link': 'http://aspn.activestate.com/ASPN/Downloads/ActivePython/'
        },
        {
            'title': 'Digital Torque Consulting Inc.',
            'link': 'http://digitaltorque.ca/'
        },
        {
            'title': "Ian Ward's Homepage",
            'link': 'http://excess.org/'
        }
    ]
    return { 'quicklinks': quick_links,
             'rootpath': rootpath }
