from django.contrib import admin
from main.models.feature import Feature


class FeatureAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'icon_name',
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