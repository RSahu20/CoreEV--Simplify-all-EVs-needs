# Generated by Django 3.0.5 on 2020-04-16 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("userapp", "0012_auto_20200416_2341"),
    ]

    operations = [
        migrations.AlterField(
            model_name="maintenancemandetails",
            name="CompletedComplaints",
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
