import pytest
from django.urls import reverse
from tests.factories import (
    CategoryFactory,
    ProductFactory,
)


@pytest.mark.django_db
def test_product(client):
    """Test product page"""

    #  Create category and its products
    category = CategoryFactory.create()
    product = ProductFactory.create(category=category)

    #  Test response status code
    url = reverse(
        'product',
        kwargs={
            'category_slug': category.category_slug,
            'product_slug': product.product_slug})
    response = client.get(url)
    assert response.status_code == 200

    product_context = response.context['product']
    assert product == product_context
