# Generated by Django 4.2.7 on 2023-11-15 12:58

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0014_alter_article_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="content",
            field=ckeditor_uploader.fields.RichTextUploadingField(
                max_length=10000, unique=True
            ),
        ),
    ]