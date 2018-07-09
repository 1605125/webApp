from django.conf.urls import url
from testApp import views


urlpatterns = [
    url(r'^hello_django$', views.helloDjango, name='hello_django'),
    url(r'^hello_django2$', views.helloDjango2, name='hello_django2')
]