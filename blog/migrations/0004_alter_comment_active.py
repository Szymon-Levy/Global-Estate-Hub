# Generated by Django 4.2.7 on 2024-01-03 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_alter_commentdislike_user_alter_commentlike_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="active",
            field=models.BooleanField(default=False),
        ),
    ]