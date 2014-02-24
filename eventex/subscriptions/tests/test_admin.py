# coding: utf-8
from django.test import TestCase
from mock import Mock

from eventex.subscriptions.admin import SubscriptionAdmin, Subscription, admin


class MarkAsPaiedTest(TestCase):
    def setUp(self):
        # Instancia o Model Admin
        self.model_admin = SubscriptionAdmin(Subscription, admin.site)

        # Creating fake data
        Subscription.objects.create(
            name='Felipe Ramos',
            cpf='12345678900',
            email='felipe@ramos.com',
            phone='24-123456789'
        )

    def test_has_action(self):
        'Action is installed'
        self.assertIn('mark_as_paid', self.model_admin.actions)

    def test_mark_all(self):
        'Mark all paied'
        fake_request = Mock()
        queryset = Subscription.objects.all()
        self.model_admin.mark_as_paid(fake_request, queryset)

        self.assertEqual(Subscription.objects.filter(paid=True).count(), 1)