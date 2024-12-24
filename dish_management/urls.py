from django.urls import path

from dish_management.views import DishListView, DishCreateView

urlpatterns = [
    path("", DishListView.as_view(), name="dish_list"),
    path("create/", DishCreateView.as_view(), name="create_dish")
]
