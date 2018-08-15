from django.contrib import admin

from .models import ReportingRawData


@admin.register(ReportingRawData)
class ReportingRawAdmin(admin.ModelAdmin):
	list_display = (
		'email', 'project_id', 'device_id', 'pin', 
		'stringvalue', 'doublevalue', 'ts')
	list_display_links = None
	list_filter = ('email',)

	search_fields = ['email', 'project_id', 'device_id', 'pin', 'ts']
