from django.views.generic import (
    CreateView,
    UpdateView,
    ListView,
    DeleteView,
    DetailView,
)

from dish_management.models import Dish


# Create your views here.
class DishCreateView(CreateView):
    model = Dish
    fields = ("name", "price", "quantity")


class DishUpdateView(UpdateView):
    model = Dish
    fields = ("name", "price", "quantity")


class DishListView(ListView):
    model = Dish
    paginate_by = 2
    template_name = "dish_management/index.html"
    context_object_name = "dishes"
