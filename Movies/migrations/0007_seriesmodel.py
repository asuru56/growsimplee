# Generated by Django 3.0.2 on 2020-07-21 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movies', '0006_movies_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='SeriesModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('discription', models.TextField(max_length=10000)),
                ('image', models.ImageField(upload_to='images/')),
                ('screen_shot', models.ImageField(upload_to='screenshots/')),
                ('series_length', models.CharField(max_length=50)),
                ('release_date', models.DateField()),
                ('series_rate', models.CharField(max_length=100)),
                ('imdb_rating', models.CharField(max_length=100)),
                ('series_director', models.CharField(max_length=200)),
                ('series_actor', models.CharField(max_length=1000)),
                ('series_language', models.CharField(max_length=100)),
                ('series_quality', models.CharField(max_length=100)),
                ('series_size', models.CharField(max_length=100)),
                ('series_subtitle', models.CharField(max_length=100)),
                ('series_type', models.CharField(max_length=200)),
                ('series_subscription', models.CharField(max_length=700)),
                ('series_category', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
                ('seasons', models.CharField(max_length=1000)),
            ],
        ),
    ]
