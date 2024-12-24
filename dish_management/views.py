from django.views.generic import (
    CreateView,
    UpdateView,
    ListView,
    DeleteView,
    DetailView,
)
from django.shortcuts import redirect

from dish_management.models import Dish


# Create your views here.
class DishCreateView(CreateView):
    model = Dish
    fields = ("name", "price", "quantity")
    template_name = "dish_management/create.html"


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


class DishDeleteView(DeleteView):
    model = Dish
    success_url = redirect("dish-list")
