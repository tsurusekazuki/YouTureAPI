# Generated by Django 2.1 on 2020-01-07 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youture', '0002_remove_youtube_category_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='youtube',
            name='category_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='カテゴリID'),
        ),
    ]
