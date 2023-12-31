# Generated by Django 4.2 on 2023-07-25 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('writers_app', '0003_remove_writer_article_alloted'),
        ('article_app', '0002_article_article_name_article_article_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='writer_alloted',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='writers_app.writer'),
        ),
    ]
