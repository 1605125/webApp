from django.conf.urls import url
from testApp import views

urlpatterns = [
    url(r'^hello_everyone$', views.helloDjango, name='hello_everyone')
]
