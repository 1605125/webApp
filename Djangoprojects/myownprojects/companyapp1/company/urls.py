from django.conf.urls import url
from company import views

urlpatterns = [
    url(r'^hello_company$', views.helloCompany)

]