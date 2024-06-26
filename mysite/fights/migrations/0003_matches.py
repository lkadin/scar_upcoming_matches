# Generated by Django 5.0.4 on 2024-04-21 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fights", "0002_rename_urls_url"),
    ]

    operations = [
        migrations.CreateModel(
            name="Matches",
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
                ("player1_name", models.CharField(max_length=100)),
                ("player2_name", models.CharField(max_length=100)),
                ("match_time", models.DateTimeField()),
                ("tournemant_name", models.CharField(max_length=100)),
            ],
        ),
    ]
