# Generated by Django 4.1 on 2022-08-24 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0002_rename_image_product_image_url"),
    ]

    operations = [
        migrations.CreateModel(
            name="Offer",
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
                ("code", models.CharField(max_length=10)),
                ("description", models.CharField(max_length=255)),
                ("discount", models.FloatField()),
            ],
        ),
    ]
