# Generated by Django 4.2.7 on 2023-12-15 14:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0098_alter_onetimepassword_expires_in"),
    ]

    operations = [
        migrations.AlterField(
            model_name="onetimepassword",
            name="expires_in",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 12, 15, 14, 39, 42, 174616, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]