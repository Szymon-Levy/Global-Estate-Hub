# Generated by Django 4.2.7 on 2024-01-17 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        (
            "properties",
            "0032_rename_propertytype_category_alter_category_options_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="property",
            name="city",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="cities",
                to="properties.city",
            ),
        ),
    ]
