from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('services/<slug:slug>/', views.service_detail_view, name='service_detail'),
    path('projects/<slug:slug>/', views.project_detail_view, name='project_detail'),
] 