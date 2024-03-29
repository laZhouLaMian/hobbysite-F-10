# Generated by Django 5.0.2 on 2024-03-19 14:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0003_alter_article_options_alter_articlecategory_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='photo',
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='articles', to='wiki.articlecategory'),
        ),
    ]
