from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # To serve static content in development.
    # Admin access
    (r'^admin/(.*)', admin.site.root),
    # Default handler is the main app.
    (r'', include('opag.main.urls'))
)
