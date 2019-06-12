"""File that contains urls tests"""
from django.test import SimpleTestCase
from django.urls import resolve, reverse
from myapp.views import *


class TestUrls(SimpleTestCase):
    """Urls tests class"""

    def test_homepage_url_is_resolved(self):
        """Test the homepage url"""
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)

    def test_leafs_url_is_resolved(self):
        """Test the leafs page url"""
        url = reverse('leafs')
        self.assertEquals(resolve(url).func, leafs)

    def test_credits_url_is_resolved(self):
        """Test the credits url"""
        url = reverse('credits')
        self.assertEquals(resolve(url).func, credits)

    def test_qcm_url_is_resolved(self):
        """Test the qcm page url"""
        url = reverse('qcm')
        self.assertEquals(resolve(url).func, qcm)
