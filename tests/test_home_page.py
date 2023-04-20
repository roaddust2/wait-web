import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_home_page(client):
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200
