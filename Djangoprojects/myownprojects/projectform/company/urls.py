from django.conf.urls import url
from company import views
from testApp import views as testviews


urlpatterns = [
    url(r'^company_app$', views.Companyapp, name='company_app'),
    url(r'^hello_hi$', testviews.hello, name='hello_hi')
]
