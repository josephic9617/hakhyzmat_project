from django.contrib import admin
from main.models.testimonial import Testimonial


class TestimonialAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'residence',
        'message',
        'image',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'name',
        'residence',
        'message',
        'created_at',
        'updated_at',
    )
    search_fields = (
        'id',
        'name',
        'residence',
        'message',
        'created_at',
        'updated_at',
    )