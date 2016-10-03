from django.contrib import admin
from .models import about, portfolio, blog, contact, media

# Register your models here.

admin.site.register(about)
admin.site.register(portfolio)
admin.site.register(blog)
admin.site.register(contact)
admin.site.register(media)
