import pytest
from django.urls import reverse
from django.core.files.storage import default_storage
from app.models.home import CarouselItem
from app.views.home import ITEMS_COUNT_CAROUSEL, ITEMS_COUNT_FEATURED
from tests.factories import (
    CarouselItemFactory,
    CategoryFactory,
    ProductFactory,
    ProductSoldFactory,
)


@pytest.fixture(autouse=True)
def cleanup_images(request):
    """Delete images associated with CarouselItem instances"""
    yield
    carousel_items = CarouselItem.objects.all()
    for item in carousel_items:
        if item.image:
            image_path = item.image.path
            default_storage.delete(image_path)


@pytest.mark.django_db
def test_index(client):
    """Test home page response"""
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_categories_context_processor(client):
    """Test categories context data"""

    #  Create Category instances
    categories = CategoryFactory.create_batch(4)

    #  Test response status code
    url = reverse('index')
    response = client.get(url)
    categories_context = response.context['categories']

    #  Test context (availible anywhere with context processor)
    assert categories[:] == categories_context[:]


@pytest.mark.django_db
def test_carousel_items(client):
    """Test carousel items on home page"""

    #  Create CarouselItem instances
    carousel_items = CarouselItemFactory.create_batch(ITEMS_COUNT_CAROUSEL + 1)

    #  Test response status code
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200

    #  Test view context
    carousel_items_context = response.context['carousel_items']
    assert len(carousel_items_context) == ITEMS_COUNT_CAROUSEL
    assert carousel_items[:-1] == carousel_items_context[:]


@pytest.mark.django_db
def test_carousel_items_order(client):
    """Test carousel items ordering on home page"""

    #  Create CarouselItem instances
    CarouselItemFactory.create_batch(ITEMS_COUNT_CAROUSEL)

    url = reverse('index')
    response = client.get(url)
    carousel_items_context = response.context['carousel_items']

    #  Test that order of items is correct
    ordering = []
    for item in carousel_items_context:
        ordering.append(item.priority)
    ordering_sorted = ordering[:]
    ordering_sorted.sort()
    assert ordering == ordering_sorted


@pytest.mark.django_db
def test_index_featured_products(client):
    """Test featured products block"""

    #  Create Product instances
    products = ProductFactory.create_batch(5)

    #  Test view context
    url = reverse('index')
    response = client.get(url)
    products_context = response.context['products']
    assert len(products_context) == ITEMS_COUNT_FEATURED
    assert products[:-1] == products_context[:]


@pytest.mark.django_db
def test_index_featured_products_order(client):
    """Test featured products block ordering, sold items in the end"""

    #  Create Product instances, first is sold (True)
    ProductSoldFactory.create_batch(1)
    ProductFactory.create_batch(3)

    #  Test view context
    url = reverse('index')
    response = client.get(url)
    products_context = response.context['products']
    assert products_context[:][-1].sold is True
