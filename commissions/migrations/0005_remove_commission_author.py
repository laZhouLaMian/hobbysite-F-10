# Generated by Django 5.0.1 on 2024-05-08 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commissions', '0004_alter_commission_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commission',
            name='author',
        ),
    ]