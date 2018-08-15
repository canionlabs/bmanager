from django.contrib import admin

from .models import Users as BUsers
from .models import ForwardingTokens


@admin.register(BUsers)
class BUsersAdmin(admin.ModelAdmin):
	list_display = ('email', 'region', 'energy', 'last_logged')


@admin.register(ForwardingTokens)
class ForwardingTokensAdmin(admin.ModelAdmin):
	list_display = ('token', 'email', 'project_id', 'device_id', 'ts')
