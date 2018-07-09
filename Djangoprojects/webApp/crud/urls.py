from django.conf.urls import url
from crud import views


urlpatterns =[
    url(r'^create$', views.create, name='create'),
    url(r'^index$', views.index, name='index'),
    url(r'^update/(?P<id>[0-9]+)$', views.update, name='update'),  # P  indicates param (+ is 1 or more)in regular expr
    # url(r'^update/(?P<id>[0-9]+)/ (?P<name>[a-z]+)$', views.update, name='update')
    url(r'^view/(?P<id>[0-9]+)$', views.view, name='view'),
    url(r'^delete/(?P<id>[0-9]+)$', views.delete, name='delete')
]

