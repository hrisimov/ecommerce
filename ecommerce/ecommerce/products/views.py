from django.shortcuts import get_object_or_404
from django.views import generic as views

from ecommerce.products.models import Product, Category


class ProductsListView(views.ListView):
    model = Product
    template_name = 'products/products_list.html'
    paginate_by = 12
    by_category = None

    def get_queryset(self):
        queryset = super().get_queryset()

        category_slug = self.kwargs.get('slug')
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            queryset = queryset.filter(category=category)
            self.by_category = category

        return queryset.prefetch_related('productimage_set')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['category'] = self.by_category
        context['categories'] = Category.objects.all()
        return context
