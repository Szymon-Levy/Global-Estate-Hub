# Generated by Django 4.2.7 on 2023-12-14 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0023_alter_category_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="active",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="comment",
            name="dislikes",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="comment",
            name="likes",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="comment",
            name="parent",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comment_parent",
                to="blog.comment",
            ),
        ),
    ]
