import json

#import requests
#from django.http import HttpResponse
#from requests.auth import HTTPBasicAuth

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
#from tanapp.credentials import MpesaAccessToken, LipanaMpesaPassword
from tanapp.models import Contacts, Comments, Quotes, Project
from tanapp.forms import ContactForm, CommentForm, QuoteForm


def home(request):
    return render(request, 'index.html')

def about(request):
    if request.method == 'POST':
        myquote = Quotes(
            name = request.POST['name'],
            email = request.POST['email'],
            phone = request.POST['phone'],
            message = request.POST['message'],
        )
        myquote.save()
        return redirect('/showquotes')
    else:
        return render(request, 'about.html')

def showquotes(request):
    allquotes = Quotes.objects.all()
    return render(request, 'showquotes.html', {'quotes': allquotes})

def deletequotes(request, id):
    myquotes = Quotes.objects.get(id=id)
    myquotes.delete()
    return redirect('/showquotes')

def editquotes(request, id):
    editquote = Quotes.objects.get(id=id)
    return render(request, 'editquotes.html', {'quotes': editquote})

def updatequotes(request, id):
    updatequoteinfo = Quotes.objects.get(id=id)
    form = QuoteForm(request.POST, instance=updatequoteinfo)
    if form.is_valid():
        form.save()
        return redirect('/showquotes')
    else:
        return render(request, 'editquotes.html')

def blogdetails(request):
    if request.method == 'POST':
        mycomments =Comments(
            name = request.POST['name'],
            email = request.POST['email'],
            website = request.POST['website'],
            comment = request.POST['comment'],
        )
        mycomments.save()
        return redirect('/showcomments')
    else:
        return render(request, 'blog-details.html')

def showcomments(request):
    allcomments = Comments.objects.all()
    return render(request, 'showcomments.html', {'comments': allcomments})

def deletecomments(request, id):
    mycomments = Comments.objects.get(id=id)
    mycomments.delete()
    return redirect('/showcomments')

def editcomments(request, id):
    editcomment = Comments.objects.get(id=id)
    return render(request, 'editcomments.html', {'comments': editcomment})

def updatecomments(request, id):
    updatecommentinfo = Comments.objects.get(id=id)
    form = CommentForm(request.POST, instance=updatecommentinfo)
    if form.is_valid():
        form.save()
        return redirect('/showcomments')
    else:
        return render(request, 'editcomments.html')

def blog(request):
    return render(request, 'blog.html')

def constructions(request):
    return render(request, 'constructions.html')

def contact(request):
    if request.method == 'POST':  # Process the form if it's a POST request
        mycontacts = Contacts(
            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message'],
        )
        mycontacts.save()  # Save the contact information to the database
        return redirect('/showcontacts')  # Redirect to the list of contacts
    else:
        return render(request, 'contact.html')  # Render the contacts page for GET requests

# Displays all contact submissions
def showcontacts(request):
    allcontacts = Contacts.objects.all()  # Fetch all contacts
    return render(request, 'showcontacts.html', {'contact': allcontacts})

# Deletes a contact submission based on its ID
def deletecontacts(request, id):
    mycontacts = Contacts.objects.get(id=id)  # Fetch the contact by ID
    mycontacts.delete()  # Delete the contact
    return redirect('/showcontacts')  # Redirect to the list of contacts

# Displays a form for editing a contact and processes updates
def editcontacts(request, id):
    editcontact = Contacts.objects.get(id=id)  # Fetch the contact by ID
    return render(request, 'editcontacts.html', {"contact": editcontact})

def updatecontacts(request, id):
    updatecontactsinfo = Contacts.objects.get(id=id)  # Fetch the contact by ID
    form = ContactForm(request.POST, instance=updatecontactsinfo)  # Bind data to the form
    if form.is_valid():  # Validate the form
        form.save()  # Save the updates
        return redirect('/showcontacts')  # Redirect to the list of contacts
    else:
        return render(request, 'editcontacts.html')  # Reload the edit page if validation fails

def projectdetails(request):
    return render(request, 'project-details.html')

def projects(request):
    return render(request, 'projects.html')

def upload_project(request):
    if request.method == 'POST':
        client_name = request.POST['client_name']
        project_type = request.POST['project_type']
        project_price = request.POST['project_price']
        project_image = request.FILES['project_image']

        # Save to database
        project = Project(
            client_name=client_name,
            project_type=project_type,
            project_price=project_price,
            project_image=project_image,
        )
        project.save()

        messages.success(request, 'Project uploaded successfully!')
        return redirect('show_projects')  # Redirect to home or any desired page

    return render(request, 'upload_project.html')

def show_projects(request):
    projects = Project.objects.all()  # Fetch all projects from the database
    return render(request, 'show_projects.html', {'projects': projects})

def delete_project(request, id):
    project = get_object_or_404(Project, id=id)
    project.delete()
    return redirect('show_projects')


def services(request):
    return render(request, 'services.html')

def starter(request):
    return render(request, 'starter-page.html')

def testimonials(request):
    return render(request, 'testimonials.html')