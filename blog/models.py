from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Post(models.Model):
    tag_list=['Job Circular','Higher Study Opportunities','Publications','Achievements','Educational Blog']
    Tag_Choices = []
    for x in tag_list:
        Tag_Choices.append((x,x))

    author = models.ForeignKey('home.Alumni_Profile',on_delete=models.CASCADE)
    body = RichTextUploadingField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    tag = models.CharField(max_length=30,choices=Tag_Choices)
    
    def __str__(self):
        return self.author.full_name

class Comment(models.Model):
    author = models.ForeignKey('home.Alumni_Profile',on_delete=models.CASCADE)
    body = RichTextUploadingField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

