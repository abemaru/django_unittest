import pytest

from rest_framework.test import APIRequestFactory
from sample.views import OnlyViews

class TestAPIViewTests:
    def test_get(self):
        factory = APIRequestFactory()
        view = OnlyViews.as_view()

        url = "http://127.0.0.1:8000/my_api/only_views"
        request = factory.get(url)

        response = view(request)
        assert response.data == ["foo", "bar"]


    def test_post(self):
        factory = APIRequestFactory()
        view = OnlyViews.as_view()

        url = "http://127.0.0.1:8000/my_api/only_views"
        request = factory.post(url, {'number': 10})

        response = view(request)
        assert response.data == 11
