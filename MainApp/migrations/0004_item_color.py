# Generated by Django 4.2.4 on 2023-08-18 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("MainApp", "0003_color"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="color",
            field=models.CharField(default="Temporary not filled", max_length=32),
        ),
    ]
