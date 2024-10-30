from django.contrib import admin
from main.models.banner import Banner


class BannerAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'description',
        'image',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'title',
        'description',
        'created_at',
        'updated_at',
    )
    search_fields = (
        'id',
        'title',
        'description',
        'created_at',
        'updated_at',
    )