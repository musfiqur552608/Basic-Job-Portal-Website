from django.contrib import admin


admin.site.site_header = 'Job Portal Admin'
admin.site.site_title = 'Job Portal Admin'
admin.site.index_title = 'Job Portal Administration'
# Register your models here.
from .models import Job, Application

admin.site.register(Job)    
admin.site.register(Application)
