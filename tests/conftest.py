import pytest
from django.core.files.storage import default_storage
from app.models.home import CarouselItem
from app.models.product import Category, ProductImage


@pytest.fixture(autouse=True)
def cleanup_images(request):
    """Delete images after tests"""
    yield
    categories = Category.objects.all()
    for category in categories:
        if category.image:
            image_path = category.image.path
            default_storage.delete(image_path)
    carousel_items = CarouselItem.objects.all()
    for item in carousel_items:
        if item.image:
            image_path = item.image.path
            default_storage.delete(image_path)
    product_images = ProductImage.objects.all()
    for item in product_images:
        if item.image:
            image_path = item.image.path
            default_storage.delete(image_path)
