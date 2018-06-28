from django.conf.urls import url
from formapp import views


urlpatterns = [
    url(r'^form_example$', views.formExample)
]