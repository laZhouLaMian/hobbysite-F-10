# Generated by Django 5.0.2 on 2024-05-04 07:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0006_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_on']},
        ),
    ]
