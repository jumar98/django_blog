from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('post_edit/<int:pk>/', views.post_edit, name='post_edit'),
]
