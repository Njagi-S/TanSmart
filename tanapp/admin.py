from django.contrib import admin
from tanapp.models import Contacts, Comments, Quotes, Project

# Register your models here.
admin.site.register(Contacts)

admin.site.register(Comments)

admin.site.register(Quotes)

admin.site.register(Project)
