from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.profile, name='profile'),
    url(r'^portfolio$', views.works, name='works'),
    url(r'^blog$', views.post_list, name='post_list'),
    url(r'^contact$', views.reach_me, name='contact'),
]