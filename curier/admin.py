from django.contrib import admin

from .models import Curier,Changes

class CurierAdmin(admin.ModelAdmin):
	list_display = ['user', 'date_of_birth', 'photo','experience','phone','is_available']

admin.site.register(Curier, CurierAdmin)
admin.site.register(Changes)
