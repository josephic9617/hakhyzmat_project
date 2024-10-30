from django.contrib import admin
from main.models.team import Team


class TeamAdmin(admin.ModelAdmin):
	list_display = (
		'id',
		'name',
		'description',
		'image',
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