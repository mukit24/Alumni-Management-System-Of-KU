from django.contrib import admin
from .models import News, News_Letter
# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    list_display = ['headline', 'news_letter' ]

admin.site.register(News,NewsAdmin)
admin.site.register(News_Letter)