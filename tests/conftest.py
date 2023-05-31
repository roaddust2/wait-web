# import pytest
# import os
# from app.models.home import CarouselItem
# from app.models.product import Category, Product, ProductImage
# from django.conf import settings


# @pytest.fixture
# def carousel_item(db):
#     item = CarouselItem.objects.create(
#         label='Label1',
#         placeholder='Placeholder1',
#         image=os.path.join(settings.STATIC_ROOT, 'images', 'carousel_empty.jpg'),
#         image_alt='alt_text',
#         priority=1,
#     )
#     return item


# @pytest.fixture
# def carousel_item_data():
#     data = {
#         'label': 'Label1',
#         'placeholder': 'Placeholder1',
#         'image': os.path.join(settings.STATIC_ROOT, 'images', 'carousel_empty.jpg'),
#         'image_alt': 'alt_text',
#         'priority': 1,
#     }
#     return data
