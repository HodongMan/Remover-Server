# Generated by Django 2.0.1 on 2018-01-15 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('views', models.PositiveIntegerField(default=0)),
                ('image_url', models.CharField(default='', max_length=200)),
                ('background_color', models.CharField(default='', max_length=200)),
                ('color', models.CharField(default='', max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-created', '-title'),
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image_url', models.CharField(default='', max_length=200)),
                ('background_color', models.CharField(default='', max_length=200)),
                ('color', models.CharField(default='', max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('board_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='board_comment', to='board.Board')),
            ],
            options={
                'ordering': ('-board_id', '-created'),
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200)),
                ('board_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='board_like', to='board.Board')),
            ],
            options={
                'ordering': ('-board_id',),
            },
        ),
        migrations.AddField(
            model_name='board',
            name='category_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='board.Category'),
        ),
    ]
