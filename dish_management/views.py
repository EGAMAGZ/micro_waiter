from django.shortcuts import get_object_or_404, redirect
from django.views.generic import (
    CreateView,
    UpdateView,
    ListView,
    DeleteView,
    DetailView,
)

from django.urls import reverse_lazy

from dish_management.forms import CreateDishForm
from dish_management.models import Dish


# Create your views here.
class DishCreateView(CreateView):
    model = Dish
    form_class = CreateDishForm
    template_name = "dish_management/create.html"
    success_url = reverse_lazy("dish-list")


class DishUpdateView(UpdateView):
    model = Dish
    fields = ("name", "price", "quantity")
    template_name = "dish_management/update.html"


class DishDetailView(DetailView):
    model = Dish
    template_name = "dish_management/detail.html"


class DishListView(ListView):
    model = Dish
    paginate_by = 2
    template_name = "dish_management/index.html"
    context_object_name = "dishes"


def delete_dish(request, pk):
    dish = get_object_or_404(Dish, pk=pk)
    dish.delete()
    return redirect('success_url')
