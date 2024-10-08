# Generated by Django 5.0.7 on 2024-07-30 16:54

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="UserPost",
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
                ("username", models.CharField(max_length=24)),
                ("text", models.CharField(max_length=1024)),
                ("file", models.FileField(upload_to="upload")),
            ],
        ),
    ]
