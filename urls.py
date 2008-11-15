from django.conf.urls.defaults import *

urlpatterns = patterns('',
    # To serve static content in development.
    # Admin access
    #(r'^admin/', include('django.contrib.admin.urls')),
    # Default handler is the main app.
    (r'', include('opag.main.urls'))
)
