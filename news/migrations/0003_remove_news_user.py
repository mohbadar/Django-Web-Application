# Generated by Django 2.0.1 on 2018-01-19 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_news_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='user',
        ),
    ]