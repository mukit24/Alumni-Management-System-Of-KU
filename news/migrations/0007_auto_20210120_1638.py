# Generated by Django 2.2.10 on 2021-01-20 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20210120_1637'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='news_letter',
        ),
        migrations.AddField(
            model_name='news',
            name='news_letter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='news', to='news.News_Letter'),
        ),
    ]
