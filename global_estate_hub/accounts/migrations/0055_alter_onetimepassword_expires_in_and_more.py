# Generated by Django 4.2.7 on 2023-11-15 11:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0054_alter_onetimepassword_expires_in_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="onetimepassword",
            name="expires_in",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 11, 15, 11, 23, 42, 524692, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.DeleteModel(name="VerificationToken",),
    ]
