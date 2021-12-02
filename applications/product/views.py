from django.views.generic import ListView

from applications.product.models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'home_page.html'
    context_object_name = 'products'
