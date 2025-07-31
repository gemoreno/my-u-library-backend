# library/admin.py
from django.contrib import admin
from .models import Book, CheckoutRecord

admin.site.register(Book)
admin.site.register(CheckoutRecord)
