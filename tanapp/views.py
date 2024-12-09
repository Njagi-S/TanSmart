import json

import requests
from django.http import HttpResponse
from requests.auth import HTTPBasicAuth

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from tanapp.credentials import MpesaAccessToken, LipanaMpesaPassword
from tanapp.models import Contacts, Comments, Quotes, Project, Member
from tanapp.forms import ContactForm, CommentForm, QuoteForm

@login_required
def home(request):
    if request.method == 'POST':  # Handle form submission for quotes
        myquote = Quotes(
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            message=request.POST['message'],
        )
        myquote.save()
        return redirect('/showquotes')  # Redirect after saving the quote

    # Handle GET request: Retrieve member details for the homepage
    member_id = request.session.get("member_id")
    member = None
    if member_id:
        try:
            member = Member.objects.get(id=member_id)
        except Member.DoesNotExist:
            pass  # Handle the case where the member does not exist (optional)

    return render(request, "index.html", {"member": member})

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

def register(request):
    if request.method == "POST":
        # Extract form data
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        # Validate passwords match
        if password != confirm_password:
            return render(request, "register.html", {"error": "Passwords do not match"})

        # Check if username or email already exists
        if Member.objects.filter(username=username).exists():
            return render(request, "register.html", {"error": "Username already taken"})
        if Member.objects.filter(email=email).exists():
            return render(request, "register.html", {"error": "Email already registered"})

        # Create and save the member
        member = Member(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
        )
        member.set_password(password)  # Hash the password
        member.save()

        return redirect("login")  # Redirect to login page after successful registration

    return render(request, "register.html")

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        try:
            # Retrieve the member
            member = Member.objects.get(username=username)

            # Check if the password is correct
            if member.check_password(password):
                # Save user in session
                request.session["member_id"] = member.id
                return redirect("index")  # Redirect to the home page
            else:
                return render(request, "login.html", {"error": "Invalid credentials"})
        except Member.DoesNotExist:
            return render(request, "login.html", {"error": "Invalid credentials"})

    return render(request, "login.html")

def logout(request):
    if "member_id" in request.session:
        del request.session["member_id"]  # Remove member from session
    return redirect("login")  # Redirect to login page

def login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if "member_id" not in request.session:
            return redirect("login")  # Redirect to login if not logged in
        return view_func(request, *args, **kwargs)
    return wrapper

def token(request):
    consumer_key = 'IQRZWUY85JSnR4MgsoBcpt4KLbEGD08L1AA2rrkKRc8MRJKP'
    consumer_secret = 'ffubtfjBk7SADV1XaAYy9YBuxAgxGsjBeQjYDMX4Lu7PLlqTBDfcAKWLk10nfiEJ'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]

    return render(request, 'token.html', {"token":validated_mpesa_access_token})

def pay(request):
    return render(request, 'pay.html')



def stk(request):
    if request.method =="POST":
        phone = request.POST['phone']
        amount = request.POST['amount']
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPassword.Business_short_code,
            "Password": LipanaMpesaPassword.decode_password,
            "Timestamp": LipanaMpesaPassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPassword.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "TanSmart Constructions",
            "TransactionDesc": "Construction Charges"
        }
        response = requests.post(api_url, json=request, headers=headers)
        return HttpResponse("Success")
        #return redirect('/show_projects')