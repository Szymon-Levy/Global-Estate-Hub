# Generated by Django 4.2.7 on 2024-01-18 11:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0055_alter_onetimepassword_expires_in"),
    ]

    operations = [
        migrations.AlterField(
            model_name="onetimepassword",
            name="expires_in",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 1, 18, 11, 19, 47, 926622, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
