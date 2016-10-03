from django.db import models
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
    # For tags
    tag_Name = models.CharField(max_length=20, null=True, blank=True, default='Uncategorised')
    # For comments
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.CharField(max_length=100, null=True, blank=True)
    message = models.TextField(null=False, blank=False)

class contact(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    Pic = models.ImageField(null=True, blank=True)
    # For contact form
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.CharField(max_length=100, null=False, blank=False)
    message = models.TextField(null=False, blank=False)

class media(models.Model):
    any_other_media = models.ImageField(blank=False, null=False)
