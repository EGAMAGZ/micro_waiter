from django.views.generic import TemplateView

# Create your views here.

class OrderManagementView(TemplateView):
    template_name = "order_management/index.html"
