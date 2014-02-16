# coding utf-8
from django.test import TestCase

from eventex.subscriptions.forms import SubscriptionForm


class SubscriptionTest(TestCase):

    def test_form_fields(self):
        'Form should 4 fields'
        form = SubscriptionForm()
        self.assertItemsEqual(['name', 'cpf', 'email', 'phone'], form.fields)