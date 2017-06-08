from django.conf.urls import url
from todo import views

urlpatterns = [
    url(r'^todo/$', views.todo_list),
    url(r'^todo/(?P<pk>[0-9]+)/$', views.todo_detail),
]