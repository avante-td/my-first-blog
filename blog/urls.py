from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:post_id>/', views.post_detail, name='post_detail'),
    path('new/', views.post_new, name='post_new'),
    path('edit/<int:post_id>/', views.post_edit, name='post_edit'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('publish/<int:post_id>/', views.post_publish, name='post_publish'),
    path('remove/<int:post_id>/', views.post_remove, name='post_remove'),
]
