from django.db import models

# Create your models here.
# Model for Contact Submissions
class Contacts(models.Model):
    name = models.CharField(max_length=100)  # Name of the person submitting the contact form.
    email = models.EmailField()  # Email address for contact purposes.
    subject = models.CharField(max_length=50)  # Subject of the contact inquiry.
    message = models.TextField()  # Message content.

    def __str__(self):
        return self.name  # Returns the name of the person when the object is printed.

# Model for Comment Submissions
class Comments(models.Model):
    name = models.CharField(max_length=100)  # Name of the person submitting the comment.
    email = models.EmailField()  # Email address for comment purposes.
    website = models.URLField(blank=True)  # Website URL (optional).
    comment = models.TextField()  # Comment content.
    
    def __str__(self):
        return self.name  # Returns the name of the person when the object is printed.

class Quotes(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    message = models.TextField()
    
    def __str__(self):
        return self.name

class Project(models.Model):
    client_name = models.CharField(max_length=100)
    project_type = models.CharField(max_length=50, choices=[
        ('Residential', 'Residential'),
        ('Commercial', 'Commercial'),
        ('Industrial', 'Industrial'),
        ('Renovation', 'Renovation'),
    ])
    project_price = models.DecimalField(max_digits=10, decimal_places=2)
    project_image = models.ImageField(upload_to='project_images/')

    def __str__(self):
        return f"{self.client_name} - {self.project_type}"