# coding: utf-8
from django.test import TestCase
from django.db import IntegrityError
from datetime import datetime

from eventex.subscriptions.models import Subscription


class SubscriptionTest(TestCase):
    def setUp(self):
        self.data = Subscription(
            name='Felipe Ramos',
            cpf='12345678900',
            email='felipe@ramos.com',
            phone='24-123456789'
        )

    def test_create(self):
        'Subscription should have name, cpf, email and phone'
        self.data.save()
        self.assertEqual(self.data.pk, 1)

    def test_has_created_at(self):
        'Subscription should have automatic created_at'
        self.data.save()
        self.assertIsInstance(self.data.created_at, datetime)

    def test_unicode(self):
        self.assertEqual(u'Felipe Ramos', unicode(self.data))


class SubscriptionUniqueTest(TestCase):
    def setUp(self):
        # Creating data for collision test
        Subscription.objects.create(
            name='Felipe Ramos',
            cpf='12345678900',
            email='felipe@ramos.com',
            phone='24-123456789'
        )

    def test_unique_cpf(self):
        'CPF should be unique'
        s = Subscription(
            name='Felipe Ramos',
            cpf='12345678900',
            email='other@email.com',
            phone='24-123456789'
        )
        self.assertRaises(IntegrityError, s.save)

    def test_unique_email(self):
        'Email should be unique'
        s = Subscription(
            name='Felipe Ramos',
            cpf='00987654321',
            email='felipe@ramos.com',
            phone='24-123456789'
        )
        self.assertRaises(IntegrityError, s.save)