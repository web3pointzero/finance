from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
(r'^static/(?P<path>.*)$', 'django.views.static.serve',
    {'document_root': '/home/ahmet/finance/static'}),
    (r'^admin/', include(admin.site.urls)),
    (r'^rsi/', 'finance.indicators.views.rsi'),
    (r'^csv2graph/', 'finance.indicators.views.csv2graph'),
)
