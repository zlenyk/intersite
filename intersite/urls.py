from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'intersite.views.index', name='index'),
    # url(r'^InterSite/', include('InterSite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^interviews/', include('interviews.urls')),
    url(r'^people/', include('people.urls')), 
    url(r'^peopleList/', 'intersite.views.people_list', name='people_list'),
)
