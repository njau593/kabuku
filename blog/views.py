from django.shortcuts import render
from django.utils import timezone
from . import models

# Create your views here.

def profile(request):
    contents = models.about.objects.all()
    return render(request, 'blog/about.html', {'contents': contents})

def works(request):
    items = models.portfolio.objects.all()
    return render(request, 'blog/portfolio.html', {'items': items})

def post_list(request):
    posts = models.blog.objects.all()
    return render(request, 'blog/blogs.html', {'posts': posts})

def reach_me(request):
    contacts = models.contact.objects.all()
    return render(request, 'blog/contact.html', {'contacts': contacts})

# View for contact form
def submit1(request):

    return render(request, 'blog/contact.html', {})

# view for comments
def submit2(request):

    return render(request, 'blog/blogs.html', {})
