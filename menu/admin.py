from django.contrib import admin
from . import models

@admin.register(models.Item)
class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ('name',),}
