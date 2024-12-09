from django import forms
from django.contrib.auth.models import User
from tanapp.models import Contacts, Comments, Quotes
# Define a form for managing Contacts data
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contacts  # Link this form to the Contacts model
        fields = '__all__'  # Include all fields from the Contacts model
        # Useful for capturing contact details like name, email, subject, and message.
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments  # Link this form to the Comments model
        fields = '__all__'  # Include all fields from the Comments model

class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quotes  # Link this form to the Quotes model
        fields = '__all__'  # Include all fields from the Quotes model

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data
