# Generated by Django 3.0 on 2020-05-09 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Scrapcoins',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
