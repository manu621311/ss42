# Generated by Django 3.0 on 2020-05-09 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20200509_1950'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='anonymous',
            field=models.BooleanField(default=False),
        ),
    ]