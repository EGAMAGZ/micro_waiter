"""
URL configuration for micro_waiter project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from dish_management.views import (
    DishListView,
    DishCreateView,
    DishUpdateView,
    DishDetailView,
    delete_dish,
)

urlpatterns = [
    path("", DishListView.as_view(), name="dish-list"),
    path("create/", DishCreateView.as_view(), name="create-dish"),
    path("<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("<int:pk>/update/", DishUpdateView.as_view(), name="update-dish"),
    path("<int:pk>/delete/", delete_dish, name="delete-dish"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
