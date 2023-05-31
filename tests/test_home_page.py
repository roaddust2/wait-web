import pytest
from django.urls import reverse


def test_pass():
    assert 1 == 1

# @pytest.mark.django_db
# def test_home_page(client):
#     url = reverse('index')
#     response = client.get(url)
#     assert response.status_code == 200


# @pytest.mark.django_db
# def test_home_page_carousel(client, carousel_item, carousel_item_data):
#     url = reverse('index')
#     response = client.get(url)
#     assert carousel_item_data['label'].encode('UTF-8') in response.content
#     assert carousel_item_data['placeholder'].encode('UTF-8') in response.content
#     assert carousel_item_data['image'].encode('UTF-8') in response.content
#     assert carousel_item_data['image_alt'].encode('UTF-8') in response.content
