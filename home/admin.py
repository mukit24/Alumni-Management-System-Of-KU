from django.contrib import admin
from .models import Alumni_Profile
# Register your models here.

class AlumniProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'student_id', 'is_verified')
    
admin.site.register(Alumni_Profile,AlumniProfileAdmin)