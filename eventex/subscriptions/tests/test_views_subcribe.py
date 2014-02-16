# coding: utf-8
from django.test import TestCase

from eventex.subscriptions.forms import SubscriptionForm


class SubscribeTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/inscricao/')

    def test_get(self):
        """
        GET /inscricao/ should return status 200
        """
        self.assertEqual(self.response.status_code, 200)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'subscriptions/subscription_form.html')

    def test_html(self):
        'Should contain html elements'
        self.assertContains(self.response, '<form')
        self.assertContains(self.response, '<input', 7)
        self.assertContains(self.response, 'type="text"', 3)
        self.assertContains(self.response, 'type="reset"')
        self.assertContains(self.response, 'type="email"')
        self.assertContains(self.response, 'type="submit"')

    def test_csrf(self):
        'Hmtl must contain csrf token'
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_has_form(self):
        'Context must have the subscription form'
        form = self.response.context['form']
        self.assertIsInstance(form, SubscriptionForm)