from django.views.generic.base import TemplateView
from app.models.home import CarouselItem
from app.models.product import Product


class IndexView(TemplateView):
    """Home page view."""

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        # Collecting carousel items
        carousel_items = CarouselItem.objects.all().order_by('priority')[:4]
        context['carousel_items'] = carousel_items

        # Collecting featured products
        products = Product.objects.all()[:4]
        context['products'] = products

        return context
