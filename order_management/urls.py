from django.urls import path

from order_management.views import OrderManagementView

urlpatterns = [
    path("", OrderManagementView.as_view(), name="order-management"),
]
