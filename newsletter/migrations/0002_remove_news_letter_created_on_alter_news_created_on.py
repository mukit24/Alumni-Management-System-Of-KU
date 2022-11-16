# Generated by Django 4.1 on 2022-11-16 05:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news_letter',
            name='created_on',
        ),
        migrations.AlterField(
            model_name='news',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
