# Generated by Django 4.2.7 on 2023-12-30 15:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="onetimepassword",
            name="expires_in",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 12, 30, 15, 51, 0, 410239, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
