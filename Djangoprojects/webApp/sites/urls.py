from django.conf.urls import url
from sites import views


urlpatterns=[
    url('^signup$', views.userRegistration, name='signup'),
    url('^signin$', views.userLogin, name='signin'),
    url('^logout$', views.userLogout, name='logout'),
    url('^dashboard$', views.userDashBoard, name='dashboard')

]
