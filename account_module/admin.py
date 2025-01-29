from django.contrib import admin
from . import models


class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'avatar','email','username']
    list_editable = ['avatar','email','username']



admin.site.register(models.User, UserAdmin)

# Register your models here.
