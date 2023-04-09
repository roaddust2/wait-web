from django.views.generic.base import TemplateView
from app.models.home import CarouselItem


class IndexView(TemplateView):
    """Home page view."""

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        carousel_items = CarouselItem.objects.all().order_by('priority')
        context['carousel_items'] = carousel_items

        return context
