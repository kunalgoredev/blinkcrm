# Generated by Django 4.2 on 2023-07-22 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website_app', '0009_remove_website_is_deleted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='website',
            name='status',
        ),
    ]
