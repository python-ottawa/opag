from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    # To serve static content in development.
    # Admin access
    (r'^admin/', include(admin.site.urls)),
    # Default handler is the main app.
    (r'', include('myproject.main.urls'))
)

if settings.DEVELOPMENT:
    # If in development mode
    urlpatterns += patterns('',
        # To serve static content in development.
        (r'^static/(?P<path>.*)$',
            'django.views.static.serve',
            {'document_root': settings.STATIC_ROOT}),
    )

handler404 = 'myproject.main.views.notfound'
handler500 = 'myproject.main.views.servererror'
