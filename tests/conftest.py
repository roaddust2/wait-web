import pytest
from app.models.home import CarouselItem
from app.models.product import Category, Product, ProductImage


@pytest.fixture(autouse=True)
def whitenoise_autorefresh(settings):
    """Skip whitenoise "No directory at" warning"""
    settings.WHITENOISE_AUTOREFRESH = True


@pytest.fixture
def carousel_item(db):
    item = CarouselItem.objects.create(
        label='Label1',
        placeholder='Placeholder1',
        image='carousel_empty.jpeg',
        image_alt='alt_text',
        priority=1,
    )
    return item


@pytest.fixture
def carousel_item_data():
    data = {
        'label':'Label1',
        'placeholder':'Placeholder1',
        'image':'carousel_empty.jpeg',
        'image_alt':'alt_text',
        'priority':1
    }
    return data
