from django import forms

from dish_management.models import Dish


class CreateDishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ["name", "price", "quantity"]

        widgets = {
            "name": forms.TextInput(
                attrs={"class": "input input-bordered w-full", "placeholder": "Nombre"}
            ),
            "price": forms.NumberInput(attrs={"class": "grow", "placeholder": "0"}),
            "quantity": forms.NumberInput(
                attrs={"class": "input input-bordered w-full"}
            ),
        }
        error_messages = {
            "name": {
                "max_length": "El nombre no puede ser mayor a 30 caracteres",
                "required": "Este campo es requerido",
            },
            "price": {
                "max_value": "El precio no puede ser mayor a 1,000",
                "min_value": "El precio no puede ser menor a 0",
                "required": "Este campo es requerido",
            },
            "quantity": {
                "max_value": "La cantidad no puede ser mayor a 1,000",
                "min_value": "La cantidad no puede ser menor a 0",
            },
        }


class UpdateDishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ["name", "price", "quantity"]

        widgets = {
            "name": forms.TextInput(
                attrs={"class": "input input-bordered w-full", "placeholder": "Nombre"}
            ),
            "price": forms.NumberInput(attrs={"class": "grow", "placeholder": "0"}),
            "quantity": forms.NumberInput(
                attrs={"class": "input input-bordered w-full"}
            ),
        }
        error_messages = {
            "name": {
                "max_length": "El nombre no puede ser mayor a 30 caracteres",
                "required": "Este campo es requerido",
            },
            "price": {
                "max_value": "El precio no puede ser mayor a 1,000",
                "min_value": "El precio no puede ser menor a 0",
                "required": "Este campo es requerido",
            },
            "quantity": {
                "max_value": "La cantidad no puede ser mayor a 1,000",
                "min_value": "La cantidad no puede ser menor a 0",
            },
        }
