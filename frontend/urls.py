from django.urls import path, re_path
from frontend import views

urlpatterns = [
    re_path(r'^.*\.html', views.pages, name='fpages'), 
    path('', views.index, name='index'),
]
