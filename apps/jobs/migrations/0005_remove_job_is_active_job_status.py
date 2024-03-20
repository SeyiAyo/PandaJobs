# Generated by Django 5.0.2 on 2024-03-20 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_remove_job_company_job_company_location_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='is_active',
        ),
        migrations.AddField(
            model_name='job',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('employed', 'Employed'), ('archived', 'Archived')], default='active', max_length=20),
        ),
    ]