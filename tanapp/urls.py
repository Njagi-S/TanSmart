from django.contrib import admin
from django.urls import path
from tanapp import views

urlpatterns = [
    # Admin interface route
    path('admin/', admin.site.urls),
    
    path('home/', views.home, name='index'),
    
    path('about/', views.about, name='about'),
    
    path('showquotes/', views.showquotes, name='showquotes'),
    
    path('deletequotes/<int:id>', views.deletequotes, name = 'deletequotes'),
    
    path('editquotes/<int:id>', views.editquotes, name='editquotes'),
    
    path('updatequotes/<int:id>', views.updatequotes, name='updatequotes'),
    
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
    
    path('upload_project/', views.upload_project, name='upload_project'),
    
    path('show_projects/', views.show_projects, name='show_projects'),
    
    path('delete_project/<int:id>/', views.delete_project, name='delete_project'),
    
    path('', views.login, name='login'),    # URL for login
    
    path('register/', views.register, name='register'),  # URL for registration
    
    path('logout/', views.logout, name='logout'),
    
    path('pay/', views.pay, name='pay'),
    
    path('stk/', views.stk, name='stk'),
    
    path('token/', views.token, name='token'),
]