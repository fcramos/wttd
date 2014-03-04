# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse as r

from eventex.core.models import Speaker, Talk


class TalkListTest(TestCase):
    def setUp(self):
        s = Speaker.objects.create(
            name='Felipe Ramos',
            slug='felipe-ramos',
            url='feliperamos.com',
            description='Web developer!'
        )
        t1 = Talk.objects.create(
            description=u'Descrição da palestra',
            title=u'Título da palestra',
            start_time='10:00'
        )
        t2 = Talk.objects.create(
            description=u'Descrição da palestra',
            title=u'Título da palestra',
            start_time='13:00'
        )
        t1.speakers.add(s)
        t2.speakers.add(s)
        self.response = self.client.get(r('core:talk_list'))

    def test_get(self):
        'GET must result in 200.'
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        'Template should be core/talk_list.html.'
        self.assertTemplateUsed(self.response, 'core/talk_list.html')

    def test_html(self):
        'Html should list talks.'
        self.assertContains(self.response, u'Título da palestra', 2)
        self.assertContains(self.response, u'Descrição da palestra', 2)
        self.assertContains(self.response, u'Felipe Ramos', 2)
        self.assertContains(self.response, u'Web developer!', 2)

    def test_morning_talks_in_context(self):
        self.assertIn('morning_talks', self.response.context)

    def test_afternoon_talks_in_context(self):
        self.assertIn('afternoon_talks', self.response.context)