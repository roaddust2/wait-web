from django.views.generic.base import TemplateView
from app.models.home import CarouselItem
from app.models.product import Product


ITEMS_COUNT_CAROUSEL = 10
ITEMS_COUNT_FEATURED = 4


class IndexView(TemplateView):
    """Home page view."""

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        # Collecting carousel items
        carousel_items = CarouselItem.objects.all().order_by('priority')[:ITEMS_COUNT_CAROUSEL]
        context['carousel_items'] = carousel_items

        # Collecting featured products
        products = Product.objects.all().order_by('sold')[:ITEMS_COUNT_FEATURED]
        context['products'] = products

        return context
