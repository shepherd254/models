from django.contrib import admin
from .models import Student, Teachers, Parents

# Register your models here.

admin.site.register(Student)
admin.site.register(Teachers)
admin.site.register(Parents)
