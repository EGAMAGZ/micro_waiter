# Generated by Django 5.1.4 on 2025-01-07 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("dish_management", "0005_remove_dish_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
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
                ("total", models.IntegerField(verbose_name="Pago total")),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Creado"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Editado"),
                ),
                (
                    "dishes",
                    models.ManyToManyField(
                        to="dish_management.dish", verbose_name="Platillos pedidos"
                    ),
                ),
            ],
        ),
    ]
