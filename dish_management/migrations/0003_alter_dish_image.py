# Generated by Django 5.1.4 on 2025-01-01 19:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "dish_management",
            "0002_alter_dish_image_alter_dish_name_alter_dish_price_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="dish",
            name="image",
            field=models.ImageField(
                error_messages={
                    "empty": "El archivo seleccionado está vacío",
                    "invalid": "El archivo seleccionado no es una imagen",
                    "invalid_image": "El archivo seleccionado no es una imagen válida",
                    "missing": "No se ha seleccionado ningún archivo",
                    "required": "Este campo es requerido",
                },
                upload_to="dishes_image/",
                validators=[
                    django.core.validators.FileExtensionValidator(
                        ["jpg", "jpeg", "png"], "Solo se permiten archivos de imagen"
                    )
                ],
                verbose_name="Imagen de Platillo",
            ),
        ),
    ]
