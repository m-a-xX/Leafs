"""File that contains views tests"""
from django.test import TestCase, Client
from django.urls import reverse
import json


class TestViews(TestCase):
    """Views tests class"""

    def test_index_GET(self):
        """Test homepage view"""
        client = Client()
        response = client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)
        
    def test_leafs_GET(self):
        """Test leafs view"""
        client = Client()
        response = client.get(reverse('leafs'))
        self.assertEquals(response.status_code, 200)
        
    def test_credits_GET(self):
        """Test legal mentions view"""
        client = Client()
        response = client.get(reverse('credits'))
        self.assertEquals(response.status_code, 200)
        
    def test_qcm_GET(self):
        """Test qcm details view"""
        client = Client()
        response = client.get(reverse('qcm'))
        self.assertEquals(response.status_code, 200)
