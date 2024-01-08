# Generated by Django 4.2.7 on 2024-01-08 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("properties", "0013_remove_property_plan_property_plan"),
    ]

    operations = [
        migrations.AlterField(
            model_name="property",
            name="plan",
            field=models.ManyToManyField(
                related_name="property_plan", to="properties.plan"
            ),
        ),
    ]
