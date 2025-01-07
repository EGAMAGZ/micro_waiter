from django.db import models
from django.core import validators

from dish_management.models import Dish


# Create your models here.
class Order(models.Model):
    total = models.IntegerField(
        verbose_name="Total",
    )
    iva = models.IntegerField(verbose_name="IVA")
    sub_total = models.IntegerField(
        verbose_name="Subtotal",
    )

    dishes = models.ManyToManyField(
        Dish,
        through="OrderDish",
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

    def save(self, *args, **kwargs):
        self.iva = int(self.sub_total * 0.16)
        self.total = self.sub_total + self.iva

        super().save(*args, **kwargs)


class OrderDish(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    quantity = models.IntegerField(
        validators=[
            validators.MinValueValidator(1),
        ],
        verbose_name="Cantidad",
        default=1,
    )
    price_unit = models.IntegerField(
        verbose_name="Precio Unitario"
    )
    iva = models.IntegerField(
        verbose_name="IVA"
    )
    total = models.IntegerField(
        verbose_name="Total"
    )

    def save(self, *args, **kwargs):
        self.price_unit = self.dish.price
        self.total = self.quantity * self.price_unit
        self.iva = int(self.total * 0.16)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.quantity}x {self.dish.name} en Orden #{self.order.id}"