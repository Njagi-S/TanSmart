from django.contrib import admin
from django.urls import path
from tanapp import views

urlpatterns = [
    # Admin interface route
    path('admin/', admin.site.urls),
    
    path('', views.home, name='index'),
    
    path('about/', views.about, name='about'),
    
    path('blogdetails/', views.blogdetails, name='blogdetails'),
    
    path('showcomments/', views.showcomments, name='showcomments'),
    
    path('deletecomments/<int:id>', views.deletecomments, name = 'deletecomments'),
    
    path('editcomments/<int:id>', views.editcomments, name='editcomments'),
    
    path('updatecomments/<int:id>', views.updatecomments, name='updatecomments'),
    
    path('blog/', views.blog, name='blog'),
    
    path('constructions/', views.constructions, name='constructions'),
    
    path('contact/', views.contact, name='contact'),
    
    path('projectdetails/', views.projectdetails, name='projectdetails'),
    
    path('projects/', views.projects, name='projects'),
    
    path('services', views.services, name='services'),
    
    path('starter/', views.starter, name='starter'),
    
    path('testimonials/', views.testimonials, name='testimonials'),
    
    # URL to show all contact inquiries.
    path('showcontacts/', views.showcontacts, name='showcontacts'),  # Calls the `showcontacts` view, named 'showcontacts'.

    # URL to delete a contact inquiry (with the contact ID as a parameter).
    path('deletecontacts/<int:id>', views.deletecontacts),  # Calls the `deletecontacts` view, deleting a contact by its ID.
    
    # URL to edit a contact inquiry (with the contact ID as a parameter).
    path('editcontacts/<int:id>', views.editcontacts, name='editcontacts'),  # Calls the `editcontacts` view, named 'editcontacts'.

    # URL to update a contact inquiry (with the contact ID as a parameter).
    path('updatecontacts/<int:id>', views.updatecontacts, name='updatecontacts'),  # Calls the `updatecontacts` view, named 'updatecontacts'.from django.contrib import admin
]