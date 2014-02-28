# coding: utf-8
from django.test import TestCase
from django.core.exceptions import ValidationError
from eventex.core.models import Speaker, Contact


class SpeakerModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker(
            name='Felipe Ramos',
            slug='felipe-ramos',
            url='http://feliperamos.com',
            description='Web developer!'
        )
        self.speaker.save()

    def teste_create(self):
        'Speaker instance should be saved'
        self.assertEqual(1, self.speaker.pk)

    def test_unicode(self):
        'Speaker string representation should be the name.'
        self.assertEqual(u'Felipe Ramos', unicode(self.speaker))


class ContactModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            name='Felipe Ramos',
            slug='felipe-ramos',
            url='http://feliperamos.com',
            description='Web developer!'
        )

    def test_email(self):
        contact = Contact.objects.create(
            speaker=self.speaker,
            kind='E',
            value='felipe@ramos.com'
        )
        self.assertEqual(1, contact.pk)

    def test_phone(self):
        contact = Contact.objects.create(
            speaker=self.speaker,
            kind='P',
            value='24-22334455'
        )
        self.assertEqual(1, contact.pk)

    def test_fax(self):
        contact = Contact.objects.create(
            speaker=self.speaker,
            kind='F',
            value='24-66778899'
        )
        self.assertEqual(1, contact.pk)

    def test_kind(self):
        'Contact kind should be limited to E, P or F.'
        contact = Contact(speaker=self.speaker, kind='A', value='B')
        self.assertRaises(ValidationError, contact.full_clean)