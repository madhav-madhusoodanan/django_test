from django.contrib import admin
from .models import Book, request_detail

admin.site.register(request_detail)
admin.site.register(Book)
