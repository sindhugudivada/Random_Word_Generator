from django.conf.urls import url
from . import views           


urlpatterns = [
    url(r'^$', views.show_random),
    url(r'^random_word', views.show_random),
    url(r'^reset/', views.reset)
]  