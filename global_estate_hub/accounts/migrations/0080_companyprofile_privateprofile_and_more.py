# Generated by Django 4.2.7 on 2023-11-28 20:13

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0079_user_is_company_user_is_private_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="CompanyProfile",
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
                ("company_id", models.IntegerField()),
                ("country", models.CharField(max_length=100, null=True)),
                ("province", models.CharField(max_length=100, null=True)),
                ("city", models.CharField(max_length=100, null=True)),
                ("street", models.CharField(max_length=100, null=True)),
                ("postal_code", models.CharField(max_length=20, null=True)),
                ("phone_number", models.CharField(max_length=150, null=True)),
                ("website_url", models.URLField(null=True)),
                ("facebook_url", models.URLField(null=True)),
                ("instagram_url", models.URLField(null=True)),
                ("linkedin_url", models.URLField(null=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Company Profile",
                "verbose_name_plural": "Company Profiles",
            },
        ),
        migrations.CreateModel(
            name="PrivateProfile",
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
                ("first_name", models.CharField(max_length=100, null=True)),
                ("last_name", models.CharField(max_length=100, null=True)),
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
                ("country", models.CharField(max_length=100, null=True)),
                ("province", models.CharField(max_length=100, null=True)),
                ("city", models.CharField(max_length=100, null=True)),
                ("street", models.CharField(max_length=100, null=True)),
                ("postal_code", models.CharField(max_length=20, null=True)),
                ("phone_number", models.CharField(max_length=150, null=True)),
                ("website_url", models.URLField(null=True)),
                ("facebook_url", models.URLField(null=True)),
                ("instagram_url", models.URLField(null=True)),
                ("linkedin_url", models.URLField(null=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Private Profile",
                "verbose_name_plural": "Private Profiles",
            },
        ),
        migrations.AlterField(
            model_name="onetimepassword",
            name="expires_in",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 11, 28, 20, 18, 40, 779035, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.DeleteModel(name="Profile",),
    ]
