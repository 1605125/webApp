from django.conf.urls import url
from loginapp import views

urlpatterns = [
    url(r'^loginpage$', views.helloDjango)
]
