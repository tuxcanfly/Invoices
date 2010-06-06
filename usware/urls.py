from django.conf.urls.defaults import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^usware/', include('usware.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     (r'^admin/', include(admin.site.urls)),
     (r'^bills/$', 'usware.bills.views.dashboard'),
     (r'^bills/login/', 'django.contrib.auth.views.login'),
     (r'^bills/logout/', 'usware.bills.views.userlogout'),
     (r'^bills/view/(?P<id>\d+)/$', 'usware.bills.views.showinvoice'),
     (r'^bills/new/', 'usware.bills.views.invoiceform'),
     (r'^bills/client/new/', 'usware.bills.views.userform'),
)
