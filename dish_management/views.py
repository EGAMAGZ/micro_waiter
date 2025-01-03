from django.shortcuts import get_object_or_404, redirect
from django.views.generic import (
    CreateView,
    UpdateView,
    ListView,
    DetailView,
)

from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from dish_management.forms import CreateDishForm, UpdateDishForm
from dish_management.models import Dish


# Create your views here.
class DishCreateView(SuccessMessageMixin, CreateView):
    model = Dish
    form_class = CreateDishForm
    template_name = "dish_management/create.html"
    success_url = reverse_lazy("dish-list")
    success_message = "<b>%(name)s </b> fue creado correctamente"


class DishUpdateView(SuccessMessageMixin, UpdateView):
    model = Dish
    form_class = UpdateDishForm
    template_name = "dish_management/update.html"
    context_object_name = "dish"
    success_url = reverse_lazy("dish-list")
    success_message = "<b>%(name)s </b> fue actualizado correctamente"


class DishDetailView(DetailView):
    model = Dish
    template_name = "dish_management/detail.html"
    context_object_name = "dish"


class DishListView(ListView):
    model = Dish
    paginate_by = 5
    template_name = "dish_management/index.html"
    context_object_name = "dishes"


def delete_dish(request, pk):
    dish = get_object_or_404(Dish, pk=pk)
    dish.delete()
    messages.success(request, f"<b>{dish.name}</b> fue eliminado correctamente")
    return redirect("dish-list")
