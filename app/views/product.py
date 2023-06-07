from django.views.generic import ListView, DetailView
from app.models.product import Category, Product


PAGINATION = 20


class ProductListView(ListView):
    """List view for all products availible"""
    model = Product
    template_name = 'catalog.html'
    context_object_name = 'products'
    ordering = ['sold']
    paginate_by = PAGINATION


class ProductCategorizedListView(ProductListView):
    """List view for products filtered by category"""

    def get_queryset(self):
        category_slug = self.kwargs.get('category_slug')
        return Product.objects.filter(category__category_slug=category_slug).order_by('sold')

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)

        # Collecting category object by its slug
        category_slug = self.kwargs.get('category_slug')
        context['category'] = Category.objects.get(category_slug=category_slug)
        return context


class ProductDetailView(DetailView):
    """Detail product view"""
    model = Product
    template_name = 'product.html'
    context_object_name = 'product'
    slug_field = 'product_slug'
    slug_url_kwarg = 'product_slug'
