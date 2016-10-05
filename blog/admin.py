from django.contrib import admin
from .models import about, portfolio, blog, contact, media, files, contact_form

# Register your models here.

admin.site.register(about)
admin.site.register(portfolio)
admin.site.register(blog)
admin.site.register(contact)
admin.site.register(media)
admin.site.register(files)
admin.site.register(contact_form)
