# Generated by Django 2.0.1 on 2018-08-05 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('declare', '0003_auto_20180805_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='declare',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
