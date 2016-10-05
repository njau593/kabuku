from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

# Create your models here.

class about(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    profile_Pic = models.ImageField(null=False, blank=True)

class portfolio(models.Model):
    item = RichTextField()

class blog(models.Model):
    post = RichTextField()
    date = models.DateTimeField(default=timezone.now)
    # For tags
    tag_Name = models.CharField(max_length=20, null=True, blank=True, default='Uncategorised')

class contact(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    Pic = models.ImageField(null=True, blank=True)

class media(models.Model):
    any_other_media = models.ImageField(blank=False, null=False)

class files(models.Model):
    my_documents = models.FileField(blank=False, null=False)

class contact_form(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.CharField(max_length=100, null=True, blank=True)
    message = models.TextField(null=False, blank=False)
