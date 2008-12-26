from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
import os

admin.autodiscover()

urlpatterns = patterns('',
    # To serve static content in development.
    # Admin access
    (r'^admin/(.*)', admin.site.root),
    # Default handler is the main app.
    (r'', include('opag.main.urls'))
)

if settings.DEVELOPMENT:
    # If in development mode
    urlpatterns += patterns('',
        # To serve static content in development.
        (r'^media/(?P<path>.*)$',
            'django.views.static.serve',
            { 'document_root': os.environ['HOME'] + '/work/opag/media' }),
    )

handler404 = 'opag.main.views.notfound'
handler500 = 'opag.main.views.servererror'
