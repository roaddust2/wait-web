import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_about(client):
    """Test home page response"""
    url = reverse('about')
    response = client.get(url)
    assert response.status_code == 200
