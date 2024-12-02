from django.contrib import admin
from django.urls import path
from tanapp import views

urlpatterns = [
    # Admin interface route
    path('admin/', admin.site.urls),
    
    path('', views.home, name='index'),
    
    path('about/', views.about, name='about'),
    
    path('blogdetails/', views.blogdetails, name='blogdetails'),
    
    path('blog/', views.blog, name='blog'),
    
    path('constructions/', views.constructions, name='constructions'),
    
    path('contact/', views.contact, name='contact'),
    
    path('projectdetails/', views.projectdetails, name='projectdetails'),
    
    path('projects/', views.projects, name='projects'),
    
    path('services', views.services, name='services'),
    
    path('servicedetails/', views.servicedetails, name='servicedetails'),
    
    path('starter/', views.starter, name='starter'),
]