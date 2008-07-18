from django.conf.urls.defaults import *
import os

handler404 = 'opag.main.views.notfound'
handler500 = 'opag.main.views.servererror'

urlpatterns = patterns('',
    # To serve static content in development.
    (r'^media/(?P<path>.*)$',
        'django.views.static.serve',
        { 'document_root': os.environ['HOME'] + '/work/opag/opag/media' }),
    # Admin access
    (r'^admin/', include('django.contrib.admin.urls')),
    # Default handler is the main app.
    (r'', include('opag.main.urls'))
)
