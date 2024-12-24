from django.urls import path

from dish_management.views import (
    DishListView,
    DishCreateView,
    DishUpdateView,
    DishDetailView,
    delete_dish
)

urlpatterns = [
    path("", DishListView.as_view(), name="dish-list"),
    path("create/", DishCreateView.as_view(), name="create-dish"),
    path("<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("<int:pk>/update/", DishUpdateView.as_view(), name="update-dish"),
    path("<int:pk>/delete/", delete_dish, name="delete-dish"),
]
