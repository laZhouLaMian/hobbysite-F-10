# Generated by Django 5.0.1 on 2024-05-08 08:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commissions', '0003_commission_author_alter_commission_status_job_and_more'),
        ('user_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commission',
            name='author',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='commission', to='user_management.profile'),
        ),
    ]