# Generated by Django 3.0 on 2020-05-09 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_anonymous'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='anonymous',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='fake',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]