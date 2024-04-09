# Generated by Django 4.2.7 on 2023-12-29 17:01

import accounts.models
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                ("username", models.CharField(max_length=50, unique=True)),
                ("email", models.EmailField(max_length=100, null=True, unique=True)),
                (
                    "image",
                    models.ImageField(
                        default="default_profile_image.jpg", upload_to="profile_images"
                    ),
                ),
                (
                    "account_type",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Individual", "Individual"),
                            ("Business", "Business"),
                        ],
                        max_length=100,
                    ),
                ),
                ("is_verified", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=True)),
                ("is_superuser", models.BooleanField(default=False)),
                ("is_staff", models.BooleanField(default=False)),
                (
                    "date_joined",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("last_login", models.DateTimeField(null=True)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={"verbose_name": "User", "verbose_name_plural": "Accounts",},
            managers=[("objects", accounts.models.CustomUserManager()),],
        ),
        migrations.CreateModel(
            name="OneTimePassword",
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
                ("password", models.CharField(max_length=20)),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "expires_in",
                    models.DateTimeField(
                        default=datetime.datetime(
                            2023,
                            12,
                            29,
                            17,
                            6,
                            17,
                            218769,
                            tzinfo=datetime.timezone.utc,
                        )
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "One Time Password",
                "verbose_name_plural": "One Time Passwords",
            },
        ),
        migrations.CreateModel(
            name="Individual",
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
                    "phone_number",
                    models.CharField(blank=True, max_length=150, null=True),
                ),
                (
                    "gender",
                    models.CharField(
                        blank=True,
                        choices=[("Male", "Male"), ("Female", "Female")],
                        max_length=100,
                    ),
                ),
                ("country", models.CharField(blank=True, max_length=100, null=True)),
                ("province", models.CharField(blank=True, max_length=100, null=True)),
                ("city", models.CharField(blank=True, max_length=100, null=True)),
                ("street", models.CharField(blank=True, max_length=100, null=True)),
                ("postal_code", models.CharField(blank=True, max_length=20, null=True)),
                ("website_url", models.URLField(blank=True, null=True)),
                ("facebook_url", models.URLField(blank=True, null=True)),
                ("instagram_url", models.URLField(blank=True, null=True)),
                ("linkedin_url", models.URLField(blank=True, null=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Individual Profile",
                "verbose_name_plural": "Individual Profiles",
            },
        ),
        migrations.CreateModel(
            name="Business",
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
                ("company_name", models.CharField(max_length=100, null=True)),
                ("company_id", models.IntegerField(null=True)),
                (
                    "phone_number",
                    models.CharField(blank=True, max_length=150, null=True),
                ),
                ("country", models.CharField(blank=True, max_length=100, null=True)),
                ("province", models.CharField(blank=True, max_length=100, null=True)),
                ("city", models.CharField(blank=True, max_length=100, null=True)),
                ("street", models.CharField(blank=True, max_length=100, null=True)),
                ("postal_code", models.CharField(blank=True, max_length=20, null=True)),
                ("website_url", models.URLField(blank=True, null=True)),
                ("facebook_url", models.URLField(blank=True, null=True)),
                ("instagram_url", models.URLField(blank=True, null=True)),
                ("linkedin_url", models.URLField(blank=True, null=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Business Profile",
                "verbose_name_plural": "Business Profiles",
            },
        ),
    ]