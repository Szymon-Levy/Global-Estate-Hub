# Generated by Django 4.2.7 on 2024-01-22 12:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0061_alter_onetimepassword_expires_in"),
    ]

    operations = [
        migrations.AlterField(
            model_name="onetimepassword",
            name="expires_in",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 1, 22, 12, 47, 0, 338786, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
