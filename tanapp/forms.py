from django import forms
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