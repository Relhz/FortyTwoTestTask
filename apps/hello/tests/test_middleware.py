# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse
from apps.hello.models import Info
from apps.hello.models import Requests


class MiddlewareTest(TestCase):

    ''' test middleware '''

    def test_middleware_records(self):

        ''' test middleware make record to the database '''

        before_request = Requests.objects.all().last()
        self.client.get(reverse('main'))
        after_request = Requests.objects.all().last()
        self.assertTrue(before_request != after_request)

    def test_middleware_correct_data(self):

        ''' test middleware make record with correct data'''

        for i in range(35):
            self.client.get(reverse('main'))
        after_request = Requests.objects.all().last()
        self.assertIn('/', after_request.path)
        self.assertEquals('GET', after_request.method)
        self.assertEquals(unicode('200'), after_request.status_code)

    def test_middleware_max_records(self):

        ''' test deleting old records from db if its amount equal 30 '''

        for i in range(35):
            self.client.get(reverse('main'))
        self.assertEqual(Requests.objects.all().count(), 30)
        request = Requests.objects.all().first()
        self.client.get(reverse('requests'))
        after_request = Requests.objects.all().first()
        self.assertTrue(request != after_request)
