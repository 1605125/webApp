from django.conf.urls import url
from details import views

urlpatterns = [
    url(r'^bio_data$', views.bio_data)

]