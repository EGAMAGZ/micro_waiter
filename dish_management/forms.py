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