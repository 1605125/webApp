from django.conf.urls import url
from testApp import views as testViews
from company import views


urlpatterns = [
    url(r'^hello_company$', views.helloCompany, name='hello_company'),
    url(r'^hello_company2$', testViews.helloDjango, name='hello_company2')

]