# Generated by Django 4.2.7 on 2023-11-28 20:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0083_companyprofile_privateprofile_remove_private_user_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="onetimepassword",
            name="expires_in",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 11, 28, 20, 40, 7, 279073, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]