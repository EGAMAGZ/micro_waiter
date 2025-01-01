from django import forms

from dish_management.models import Dish


class CreateDishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ["name", "price", "quantity", "image"]

        widgets = {
            "name": forms.TextInput(
                attrs={"class": "input input-bordered w-full", "placeholder": "Nombre"}
            ),
            "price": forms.NumberInput(attrs={"class": "grow", "placeholder": "0"}),
            "quantity": forms.NumberInput(
                attrs={"class": "input input-bordered w-full"}
            ),
            "image": forms.FileInput(
                attrs={
                    "class": "w-full h-full opacity-0 absolute inset-0 cursor-pointer"
                }
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
            "image": {
                "required": "Este campo es requerido",
                "invalid": "El archivo seleccionado no es una imagen",
                "missing": "No se ha seleccionado ningún archivo",
                "empty": "El archivo seleccionado está vacío",
                "invalid_extension": "Solo se admiten archivos de imagen con extensión .jpg, .jpeg o .png",
            },
        }


class UpdateDishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ["name", "price", "quantity", "image"]

        widgets = {
            "name": forms.TextInput(
                attrs={"class": "input input-bordered w-full", "placeholder": "Nombre"}
            ),
            "price": forms.NumberInput(attrs={"class": "grow", "placeholder": "0"}),
            "quantity": forms.NumberInput(
                attrs={"class": "input input-bordered w-full"}
            ),
            "image": forms.FileInput(
                attrs={
                    "class": "w-full h-full opacity-0 absolute inset-0 cursor-pointer"
                }
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
            "image": {
                "required": "Este campo es requerido",
                "invalid": "El archivo seleccionado no es una imagen",
                "missing": "No se ha seleccionado ningún archivo",
                "empty": "El archivo seleccionado está vacío",
                "invalid_extension": "Solo se admiten archivos de imagen con extensión .jpg, .jpeg o .png",
            },
        }
