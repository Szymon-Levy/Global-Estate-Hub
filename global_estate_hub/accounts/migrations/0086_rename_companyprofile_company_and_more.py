# Generated by Django 4.2.7 on 2023-11-28 20:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0085_alter_onetimepassword_expires_in"),
    ]

    operations = [
        migrations.RenameModel(old_name="CompanyProfile", new_name="Company",),
        migrations.RenameModel(old_name="PrivateProfile", new_name="Private",),
        migrations.AlterField(
            model_name="onetimepassword",
            name="expires_in",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 11, 28, 20, 42, 13, 775902, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
