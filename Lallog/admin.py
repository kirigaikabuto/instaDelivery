from django.contrib import admin

from .models import Lalo,TestOrder



class PostAdmin(admin.ModelAdmin):
	list_display=('author', 'title','otkuda')
	list_filter=('published_date','created_date')
	"""docstring for PostAdmin"""


admin.site.register(Lalo,PostAdmin)
admin.site.register(TestOrder)