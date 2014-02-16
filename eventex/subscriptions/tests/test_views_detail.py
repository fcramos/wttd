# coding: utf-8
from django.test import TestCase

from eventex.subscriptions.models import Subscription


class DetailTest(TestCase):
    def setUp(self):
        data = Subscription.objects.create(
            name='Felipe Ramos',
            cpf='12345678900',
            email='felipe@ramos.com',
            phone='24-123456789'
        )
        self.response = self.client.get('/inscricao/%d/' % data.pk)

    def test_get(self):
        'GET /inscricao/1/ should return 200'
        self.assertEqual(self.response.status_code, 200)

    def test_view_detail(self):
        'Uses template'
        self.assertTemplateUsed(self.response, 'subscriptions/subscription_detail.html')

    def test_context(self):
        'Context must have a subscription instance'
        subscription = self.response .context['subscription']
        self.assertIsInstance(subscription, Subscription)

    def test_html(self):
        'Check is a subscription data was rendered'
        self.assertContains(self.response, 'Felipe Ramos')


class DetailNotFound(TestCase):
    def not_found(self):
        response = self.client.get('/inscricao/0/')
        self.assertEqual(response.status_code, 404)