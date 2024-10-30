from django.contrib import admin
from main.models.service import Service


class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'image',
        'description',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'name',
        'description',
        'created_at',
        'updated_at',
    )
    search_fields = (
        'id',
        'name',
        'description',
        'created_at',
        'updated_at',
    )