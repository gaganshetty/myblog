from django.contrib import admin
from . import models

class EntryAdmin(admin.ModelAdmin):
	list_display=['title','body','created']
	class Media:
		js = (
			'/static/js/jquery-2.2.4.min.js',
			'/static/ckeditor/ckeditor.js',
			'/static/js/custom.js',
		)
		css = {
            'all': ('/static/css/custom.css',)
        }

	
admin.site.register(models.Entry, EntryAdmin)

