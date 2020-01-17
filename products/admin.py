#!/bin/python3

from django.contrib import admin

from .models import Product  # .models == relative imports

# Register your models here.
admin.site.register(Product)
