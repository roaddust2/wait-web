from django.views.generic import ListView, DetailView
from app.models.product import Category, Product


class ProductListView(ListView):
    model = Product
    template_name = 'catalog.html'
    context_object_name = 'products'
    paginate_by = 20

    def get_queryset(self):
        category_name = self.kwargs.get('category')
        if category_name:
            return Product.objects.filter(category__name=category_name)
        else:
            return Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)

        category_name = self.kwargs.get('category')
        if category_name:
            context['category'] = Category.objects.get(name=category_name)
        else:
            context['categories'] = Category.objects.all()
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product'
