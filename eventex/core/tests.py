# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse as r


class HomeTest(TestCase):
    def setUp(self):
        self.response = self.client.get(r('core:home'))

    def test_get(self):
        """
        GET / should return status 200
        """
        self.assertEqual(self.response.status_code, 200)

    def test_template(self):
        """
        Should get index.html template
        """
        self.assertTemplateUsed(self.response, 'index.html')