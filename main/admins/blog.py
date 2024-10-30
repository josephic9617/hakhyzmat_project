from django.contrib import admin
from main.models.blog import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'content',
        'image',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'title',
        'content',
        'created_at',
        'updated_at',
    )
    search_fields = (
        'id',
        'title',
        'content',
        'created_at',
        'updated_at',
    )