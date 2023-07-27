# Generated by Django 4.2 on 2023-07-25 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article_app', '0002_article_article_name_article_article_status_and_more'),
        ('writers_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='writer',
            name='article_alloted',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='article_app.article'),
        ),
    ]