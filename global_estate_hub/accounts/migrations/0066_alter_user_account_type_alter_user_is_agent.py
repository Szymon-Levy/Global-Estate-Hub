# Generated by Django 4.2.7 on 2024-02-20 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0065_remove_onetimepassword_expires_in"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="account_type",
            field=models.CharField(
                blank=True,
                choices=[("Individual", "Individual"), ("Business", "Business")],
                default="Individual",
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="user", name="is_agent", field=models.BooleanField(default=True),
        ),
    ]
