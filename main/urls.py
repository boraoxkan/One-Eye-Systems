# main/urls.py

from django.urls import path
from . import views

app_name = 'main' # URL'leri isimlendirmek için namespace

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about-us/', views.AboutUsView.as_view(), name='about_us'),
    path('contact/', views.ContactView.as_view(), name='contact'),

    path('services/', views.ServiceListView.as_view(), name='service_list'),
    path('services/<slug:slug>/', views.ServiceDetailView.as_view(), name='service_detail'),

    path('projects/', views.ProjectListView.as_view(), name='project_list'),
    path('projects/<slug:slug>/', views.ProjectDetailView.as_view(), name='project_detail'),

    path('news/', views.NewsListView.as_view(), name='news_list'),
    path('news/<slug:slug>/', views.NewsDetailView.as_view(), name='news_detail'),
]