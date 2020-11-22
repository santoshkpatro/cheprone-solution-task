from django.urls import path
from .import views

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('add/', views.add_view, name='add_view'),
    path('delete/<int:user_id>/', views.delete_view, name='delete_view'),
    path('edit/<int:user_id>/', views.edit_view, name='edit_view')
]