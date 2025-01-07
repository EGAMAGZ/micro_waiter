from django.db import models

from dish_management.models import Dish


# Create your models here.
class Order(models.Model):
    total = models.IntegerField(
        verbose_name="Pago total",
    )

    dishes = models.ManyToManyField(
        Dish,
        verbose_name="Platillos pedidos",
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
