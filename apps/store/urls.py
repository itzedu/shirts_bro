from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^main$', views.main),
    url(r'^logout$', views.logout),
    url(r'^new_shirt$', views.new_shirt),
    url(r'^create_shirt$', views.create_shirt),
    url(r'^shirts/(?P<shirt_id>\d+)$', views.show_shirt),
    url(r'^delete_shirt/(?P<shirt_id>\d+)$', views.delete_shirt),
]