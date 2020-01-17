from django.contrib import admin

# Register your models here.
from .models import Article

# Register Article to be present on website
admin.site.register(Article)
