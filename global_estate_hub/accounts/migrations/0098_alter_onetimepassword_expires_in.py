# Generated by Django 4.2.7 on 2023-12-14 19:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0097_alter_onetimepassword_expires_in"),
    ]

    operations = [
        migrations.AlterField(
            model_name="onetimepassword",
            name="expires_in",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 12, 14, 19, 39, 10, 517224, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
