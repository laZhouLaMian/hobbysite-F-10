# Generated by Django 5.0.2 on 2024-03-11 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='photo',
            field=models.CharField(default='', max_length=9999),
        ),
    ]
