# Generated by Django 2.0.1 on 2018-01-15 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='board',
            name='vies',
        ),
        migrations.AddField(
            model_name='board',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
