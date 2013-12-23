from django.conf.urls import patterns, include, url
from people import views

urlpatterns = patterns('',
    url(r'^show/(?P<id>\w+)/$',views.show_person),
)
