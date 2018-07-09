# Generated by Django 2.0.1 on 2018-07-09 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0013_auto_20180630_1531'),
        ('declare', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='declare',
            name='board_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='board_declare', to='board.Board'),
        ),
    ]
