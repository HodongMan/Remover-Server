# Generated by Django 2.0.1 on 2018-03-28 03:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0009_auto_20180328_0310'),
    ]

    operations = [
        migrations.RenameField(
            model_name='board',
            old_name='user',
            new_name='user_id',
        ),
    ]
