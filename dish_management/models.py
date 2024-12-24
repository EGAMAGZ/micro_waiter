from typing import Self
from django.db import models
from django.core import validators


# Create your models here.
class Dish(models.Model):
    name = models.CharField(max_length=30, verbose_name="Nombre de Platillo")
    price = models.IntegerField(
        validators=[
            validators.MinValueValidator(0),
            validators.MaxValueValidator(1_000),
        ],
        verbose_name="Precio de Platillo",
    )
    quantity = models.IntegerField(
        validators=[
            validators.MinValueValidator(0),
            validators.MaxValueValidator(1_000),
        ],
        blank=True,
        default=0,
        verbose_name="Cantidad de Platillo",
    )
    image = models.ImageField(
        upload_to="dishes_image/", verbose_name="Imagen de Platillo"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Creado",
        editable=False,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Editado",
        editable=False,
    )

    class Meta:
        ordering = ["created_at"]

    def __str__(self: Self):
        return self.name
