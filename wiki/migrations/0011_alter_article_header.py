# Generated by Django 5.0.2 on 2024-05-06 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0010_alter_article_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='header',
            field=models.ImageField(default=None, null=True, upload_to='images/'),
        ),
    ]
