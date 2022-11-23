from django.db import models
from datetime import datetime 

# Create your models here.
class Event(models.Model):
    discipline_list = ['Architecture','CSE','ECE','Math','URP','Physics','Chemistry','Stat','Pharmacy','BGE','FWT','FMRT','Agrotechnology','ES','SWE','BAD','HRM','DP','PM','DS','History','English','Bangla','IER','Sculpture','Econ','Sociology','MCJ','Law']

    Discipline_Choices = []
    for x in discipline_list:
        Discipline_Choices.append((x,x))


    headline = models.CharField(max_length=200)
    description = models.TextField()
    created_on = models.DateTimeField(default=datetime.now)
    discipline = models.CharField(max_length=255,choices=Discipline_Choices,blank=True)
    target_amount = models.DecimalField(max_digits=15, decimal_places=2)
    present_amount = models.DecimalField(max_digits=15, decimal_places=2,default=0)
    running = models.BooleanField(default=True)

    def __str__(self):
        return self.headline

class Contributer(models.Model):
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    created_on = models.DateTimeField(default=datetime.now)
    event = models.ForeignKey('Event',on_delete=models.CASCADE)
    alumni = models.ForeignKey('home.Alumni_Profile',on_delete=models.CASCADE)

    def __str__(self):
        return self.alumni.full_name
