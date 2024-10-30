from django.contrib import admin
from main.models.contactus import ContactUs


class ContactUsAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
        'name', 
        'email', 
        'phone', 
        'subject', 
        'message', 
        'created_at', 
        'updated_at'
        )
    list_filter = (
        'name', 
        'email', 
        'phone', 
        'subject', 
        'message', 
        'created_at', 
        'updated_at'
        )
    search_fields = (
        'name', 
        'email', 
        'phone', 
        'subject', 
        'message', 
        'created_at', 
        'updated_at'
        )