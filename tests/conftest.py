import pytest


@pytest.fixture(autouse=True)
def whitenoise_autorefresh(settings):
    """Skip whitenoise "No directory at" warning"""
    settings.WHITENOISE_AUTOREFRESH = True
