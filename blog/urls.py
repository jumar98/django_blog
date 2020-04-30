from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('post_edit/<int:pk>/', views.post_edit, name='post_edit'),
    path('post/add', views.create_post, name='create_post'),
    path('post/delete/<int:pk>', views.post_delete, name='post_delete'),
    path('post/detail/<int:pk>', views.post_detail, name='post_detail')
]
