# Generated by Django 3.1 on 2021-05-02 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movies', '0020_auto_20200726_1200'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='tmvdbid',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]