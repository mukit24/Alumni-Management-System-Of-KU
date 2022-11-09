from django.contrib import admin
from .models import Event
# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ['headline', 'running', 'target_amount', 'present_amount']

admin.site.register(Event,EventAdmin)