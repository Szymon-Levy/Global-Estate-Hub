# Generated by Django 4.2.7 on 2023-11-12 21:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0035_alter_onetimepassword_expires_in"),
    ]

    operations = [
        migrations.AlterField(
            model_name="onetimepassword",
            name="expires_in",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 11, 12, 21, 30, 27, 493771, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
