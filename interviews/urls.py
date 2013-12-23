from django.conf.urls import patterns, include, url
from interviews import views

urlpatterns = patterns('',
    url(r'^show/(?P<id>\w+)/$',views.show_interview),
    url(r'^add_comment/',views.add_comment),
)
