from django import forms

from dish_management.models import Dish


class CreateDishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ["name", "price", "quantity", "image"]

        widgets = {
            "name": forms.TextInput(attrs={"class": "input input-bordered w-full"}),
            "price": forms.NumberInput(attrs={"class": "input input-bordered w-full"}),
            "quantity": forms.NumberInput(
                attrs={"class": "input input-bordered w-full"}
            ),
            "image": forms.FileInput(
                attrs={"class": "file-input file-input-bordered w-full"}
            ),
        }
