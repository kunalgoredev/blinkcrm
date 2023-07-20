# Generated by Django 4.2 on 2023-07-20 05:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website_app', '0004_website_date_created_website_updated_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(blank=True, max_length=100, null=True)),
                ('company_address', models.CharField(blank=True, max_length=100, null=True)),
                ('company_contact', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WebsiteBusinessModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_model', models.CharField(blank=True, max_length=100, null=True)),
                ('business_company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='website_app.company')),
            ],
        ),
        migrations.AlterField(
            model_name='website',
            name='status',
            field=models.CharField(blank=True, choices=[('Active', 'Active'), ('InActive', 'InActive')], default='Active', max_length=10),
        ),
        migrations.CreateModel(
            name='WebsiteBusinesstype',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(blank=True, max_length=100, null=True)),
                ('model_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='website_app.websitebusinessmodel')),
            ],
        ),
    ]
