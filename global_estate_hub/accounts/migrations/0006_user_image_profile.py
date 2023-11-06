# Generated by Django 4.2.6 on 2023-11-06 19:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0005_remove_user_is_verified"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="image",
            field=models.ImageField(
                default="default_profile_image.jpg", upload_to="profile_images"
            ),
        ),
        migrations.CreateModel(
            name="Profile",
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
                ("first_name", models.CharField(blank=True, max_length=100, null=True)),
                ("last_name", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "gender",
                    models.CharField(
                        choices=[
                            ("Not Defined", "Not Defined"),
                            ("Male", "Male"),
                            ("Female", "Female"),
                        ],
                        max_length=100,
                    ),
                ),
                ("country", models.CharField(blank=True, max_length=100, null=True)),
                ("province", models.CharField(blank=True, max_length=100, null=True)),
                ("city", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"verbose_name": "Profile", "verbose_name_plural": "Profiles",},
        ),
    ]
