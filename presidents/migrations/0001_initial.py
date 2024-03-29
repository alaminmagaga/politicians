# Generated by Django 4.2.1 on 2023-11-01 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="President",
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
                ("name", models.CharField(max_length=50, null=True)),
                (
                    "image",
                    models.ImageField(null=True, upload_to="profile_images/president"),
                ),
                ("details", models.CharField(max_length=1500, null=True)),
                (
                    "health_rating",
                    models.PositiveIntegerField(
                        choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1
                    ),
                ),
                (
                    "education_rating",
                    models.PositiveIntegerField(
                        choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1
                    ),
                ),
                (
                    "security_rating",
                    models.PositiveIntegerField(
                        choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1
                    ),
                ),
                (
                    "infrastructure_rating",
                    models.PositiveIntegerField(
                        choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1
                    ),
                ),
            ],
        ),
    ]
