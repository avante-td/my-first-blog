from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/(?P<pk>[0-9]+)/', views.post_detail, name='post_detail'),
]
