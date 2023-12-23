# Generated by Django 4.2.7 on 2023-12-20 17:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("blog", "0033_commentlike_commentdislike"),
    ]

    operations = [
        migrations.CreateModel(
            name="CommentFeedback",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[("L", "Like"), ("D", "Dislike")], max_length=1
                    ),
                ),
                (
                    "comment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="feedback",
                        to="blog.comment",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="feedback",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.RemoveField(model_name="commentlike", name="comment",),
        migrations.RemoveField(model_name="commentlike", name="user",),
        migrations.DeleteModel(name="CommentDislike",),
        migrations.DeleteModel(name="CommentLike",),
    ]
