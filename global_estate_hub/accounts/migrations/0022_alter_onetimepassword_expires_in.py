# Generated by Django 4.2.7 on 2024-01-08 09:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0021_alter_onetimepassword_expires_in"),
    ]

    operations = [
        migrations.AlterField(
            model_name="onetimepassword",
            name="expires_in",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 1, 8, 9, 9, 57, 760339, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
