import json

#import requests
#Sfrom django.http import HttpResponse
#from requests.auth import HTTPBasicAuth

from django.shortcuts import render, redirect, get_object_or_404
#from tanapp.credentials import MpesaAccessToken, LipanaMpesaPassword
#from tanapp.models import BookTable, ContactTable,Member, ImageModel
#from tanapp.forms import BookTableForm, ContactTableForm, ImageUploadForm


def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def blogdetails(request):
    return render(request, 'blog-details.html')

def blog(request):
    return render(request, 'blog.html')

def constructions(request):
    return render(request, 'constructions.html')

def contact(request):
    return render(request, 'contact.html')

def projectdetails(request):
    return render(request, 'project-details.html')

def projects(request):
    return render(request, 'projects.html')

def services(request):
    return render(request, 'services.html')

def starter(request):
    return render(request, 'starter-page.html')

def testimonials(request):
    return render(request, 'testimonials.html')