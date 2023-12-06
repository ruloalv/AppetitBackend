# Generated by Django 4.2.7 on 2023-12-04 17:34

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("username", models.CharField(max_length=30)),
                ("subjetc", models.CharField(max_length=100)),
                ("comment", models.CharField(max_length=500)),
                ("date", models.DateField(auto_now=True)),
            ],
            options={
                "db_table": "comments",
            },
        ),
    ]