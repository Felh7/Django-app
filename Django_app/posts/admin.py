from django.contrib import admin
from .models import UserPost


@admin.register(UserPost)
class AuthorAdmin(admin.ModelAdmin):
    pass