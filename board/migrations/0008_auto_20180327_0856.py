# Generated by Django 2.0.1 on 2018-03-27 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0007_auto_20180327_0848'),
    ]

    operations = [
        migrations.RenameField(
            model_name='board',
            old_name='user',
            new_name='user_id',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='user',
            new_name='user_id',
        ),
    ]
