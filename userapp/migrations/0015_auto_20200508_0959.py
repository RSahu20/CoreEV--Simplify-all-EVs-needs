# Generated by Django 3.0.5 on 2020-05-08 04:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("userapp", "0014_support"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="chargingstation",
            options={"ordering": ["-created_at"]},
        ),
    ]
