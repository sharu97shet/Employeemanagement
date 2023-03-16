from django.contrib import admin

from .models import Department, Emp

# Register your models here.

admin.site.register(Emp)

admin.site.register(Department)
