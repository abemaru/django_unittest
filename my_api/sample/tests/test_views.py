import pytest

from rest_framework.test import APIRequestFactory
from sample.views import OnlyViews

class APIViewTests:
    def test_get(self):
        factory = APIRequestFactory()
        view = OnlyViews.as_view()

        url = "http://127.0.0.1:8000/my_api/only_views"
        request = factory.get(url)

        response = view(request)
        assert response == ["foo", "bar"]
