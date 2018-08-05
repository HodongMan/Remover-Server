# Generated by Django 2.0.1 on 2018-08-05 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('declare', '0002_declare_board_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='declare',
            name='board_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='board_declare', to='board.Board'),
        ),
    ]
