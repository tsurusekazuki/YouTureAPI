from django.contrib import admin

from .models import User, Youtube


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Youtube)
class YouTube(admin.ModelAdmin):
    pass
