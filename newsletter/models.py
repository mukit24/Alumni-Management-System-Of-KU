from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from datetime import datetime 
# Create your models here.

class News(models.Model):
    headline = models.CharField(max_length=200)
    description = RichTextUploadingField()
    news_letter = models.ForeignKey('News_Letter',on_delete=models.CASCADE,related_name='news')
    created_on = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.headline


class News_Letter(models.Model):
    title = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.title
    
    
    

