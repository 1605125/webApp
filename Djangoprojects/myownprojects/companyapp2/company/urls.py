from django.conf.urls import url
from company import views
from testApp import views as testappviews


urlpatterns = [
    url(r'^hello_company$', views.company, name='hello_company'),
    url(r'^hello_everyone$', testappviews.helloDjango, name='hello_everyone')
        ]



