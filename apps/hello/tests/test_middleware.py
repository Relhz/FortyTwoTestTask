
# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse
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
