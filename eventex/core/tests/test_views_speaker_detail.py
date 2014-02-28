# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse as r

from eventex.core.models import Speaker


class SpeakerDetailTest(TestCase):
    def setUp(self):
        Speaker.objects.create(
            name='Felipe Ramos',
            slug='felipe-ramos',
            url='http://feliperamos.com',
            description='Web developer!'
        )
        url = r('core:speaker_detail', kwargs={'slug': 'felipe-ramos'})
        self.response = self.client.get(url)

    def test_get(self):
        'GET should result in 200.'
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        'Template should be core/speaker_detail.html'
        self.assertTemplateUsed(self.response, 'core/speaker_detail.html')

    def test_html(self):
        'Html must contain data.'
        self.assertContains(self.response, 'Felipe Ramos')
        self.assertContains(self.response, 'Web developer!')
        self.assertContains(self.response, 'http://feliperamos.com')

    def test_context(self):
        'Speaker must be in context.'
        speaker = self.response.context['speaker']
        self.assertIsInstance(speaker, Speaker)

class SpeakerDetailNotFound(TestCase):
    def test_not_found(self):
        url = r('core:speaker_detail', kwargs={'slug': 'john'})
        response = self.client.get(url)
        self.assertEqual(404, response.status_code)