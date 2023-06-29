import pytest
from django.urls import reverse
from app.views.product import PAGINATION
from tests.factories import (
    CategoryFactory,
    ProductFactory,
)


@pytest.mark.django_db
def test_catalog(client):
    """Test home page response"""
    url = reverse('catalog')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_catalog_featured_products(client):
    """Test catalog with featured products"""

    #  Create category and its products
    category = CategoryFactory.create()
    products = ProductFactory.create_batch(PAGINATION + 1, category=category)

    #  Test response status code
    url = reverse('catalog')
    response = client.get(url)
    assert response.status_code == 200

    #  Test context
    categories_context = response.context['categories']
    products_context = response.context['products']
    assert category == categories_context[0]
    assert products[:PAGINATION] == products_context[:]

    #  Test pagination
    assert response.context['paginator'].num_pages > 1


@pytest.mark.django_db
def test_category_with_product(client):
    """Test category with related products"""

    #  Create category and its products
    category = CategoryFactory.create()
    products = ProductFactory.create_batch(2, category=category)

    #  Test response status code
    url = reverse('category', kwargs={'category_slug': category.category_slug})
    response = client.get(url)
    assert response.status_code == 200

    products_context = response.context['products']
    assert products[:] == products_context[:]
