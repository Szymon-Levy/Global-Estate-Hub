# Generated by Django 4.2.7 on 2023-11-21 22:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0068_alter_onetimepassword_expires_in"),
    ]

    operations = [
        migrations.AlterField(
            model_name="onetimepassword",
            name="expires_in",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 11, 21, 22, 5, 45, 547016, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]