# Generated by Django 4.2.7 on 2023-11-11 15:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0025_onetimepassword_expires_in"),
    ]

    operations = [
        migrations.AlterField(
            model_name="onetimepassword",
            name="expires_in",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 11, 11, 15, 20, 4, 733930, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]