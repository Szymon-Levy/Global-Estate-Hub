# Generated by Django 4.2.7 on 2023-12-20 18:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0108_alter_onetimepassword_expires_in"),
    ]

    operations = [
        migrations.AlterField(
            model_name="onetimepassword",
            name="expires_in",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 12, 20, 18, 15, 22, 937971, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
