# coding: utf-8
from django.test import TestCase

from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription


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


class SubscribePostTest(TestCase):
    def setUp(self):
        data = dict(
            name='Felipe Ramos',
            cpf='12345678900',
            email='felipe@ramos.com',
            phone='24-123456789'
        )
        self.response = self.client.post('/inscricao/', data)

    def test_post(self):
        'Valid POST should redirect to /inscricao/1'
        self.assertEqual(self.response.status_code, 302)

    def test_save(self):
        'Valid POST must have saved'
        self.assertTrue(Subscription.objects.exists())


class SubscribeInvalidPostTest(TestCase):
    def setUp(self):
        data = dict(
            name='Felipe Ramos',
            cpf='000987654321',
            email='felipe@ramos.com',
            phone='24-123456789'
        )
        self.response = self.client.post('/inscricao/', data)

    def test_post(self):
        'Invalid POST should not redirect'
        self.assertEqual(self.response.status_code, 200)

    def test_form_errors(self):
        'Form must contain errors'
        self.assertTrue(self.response.context['form'].errors)

    def test_dont_save(self):
        'Do not save data'
        self.assertFalse(Subscription.objects.exists())