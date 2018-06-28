from django.conf.urls import url
from musicApp import views

urlpatterns = [
    url(r'^hellomusic', views.hellodjango)

]
