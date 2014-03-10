# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse as r

from eventex.core.models import Talk


class TalkDetailTest(TestCase):
    def setUp(self):
        t = Talk.objects.create(title='Talk', start_time='10:00')
        t.speakers.create(name='Felipe Ramos', slug='felipe-ramos')
        self.response = self.client.get(r('core:talk_detail', args=[1]))

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'core/talk_detail.html')

    def test_talk_in_context(self):
        talk = self.response.context['talk']
        self.assertIsInstance(talk, Talk)

    def test_not_found(self):
        response = self.client.get(r('core:talk_detail', args=[0]))
        self.assertEqual(404, response.status_code)

    def test_html(self):
        self.assertContains(self.response, 'Talk')
        self.assertContains(self.response, '/palestrantes/felipe-ramos/')
        self.assertContains(self.response, 'Felipe Ramos')