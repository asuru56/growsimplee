# Generated by Django 3.0.2 on 2020-07-20 16:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Movies', '0005_auto_20200720_2210'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
