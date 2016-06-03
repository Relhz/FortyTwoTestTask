# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse
from apps.hello.models import Info
from apps.hello.models import Requests


class MainPageViewTest(TestCase):

    ''' testing view for main page '''

    def test_root_url_template(self):

        ''' test using template '''

        response = self.client.get(reverse('main'))
        self.assertTemplateUsed(response, 'base.html')

    def test_main_page(self):

        ''' test status code '''

        response = self.client.get(reverse('main'))
        self.assertEquals(response.status_code, 200)

    def test_content_info(self):

        ''' test view renders required data '''

        response = self.client.get(reverse('main'))
        self.assertIn('<h1>42 Coffee Cups Test Assignment</h1>',
                      response.content)
        self.assertIn('Skype', response.content)
        self.assertTrue('info' in response.context)

    def test_render_all_fields(self):

        ''' test does all fields render '''

        response = self.client.get(reverse('main'))
        info = Info.objects.get(last_name='Kudrya')

        self.assertIn(info.name, response.content)
        self.assertIn(info.last_name, response.content)
        self.assertIn('Jan. 21, 1990', response.content)
        self.assertIn(info.bio, response.content)
        self.assertIn(info.contacts, response.content)
        self.assertIn(info.email, response.content)
        self.assertIn(info.skype, response.content)
        self.assertIn(info.jabber, response.content)
        self.assertIn(info.other_contacts, response.content)

    def test_render_cyrillic(self):

        ''' test does cyrillic symbols render'''

        info = Info.objects.get(last_name='Kudrya')
        info.name = 'Євген'
        info.save()
        response = self.client.get(reverse('main'))
        self.assertIn(info.name, response.content)

    def test_if_object_does_not_exists(self):

        ''' test if object doesn't exists'''

        info = Info.objects.all().delete()

        response = self.client.get(reverse('main'))
        self.assertTrue('info' in response.context)
        context = response.context['info']
        self.assertTrue(context.last_name == 'Surname')
        self.assertContains(response, 'Surname', count=1, status_code=200)
        self.assertTrue(context.name is None)

    def test_if_several_objects_in_db(self):

        ''' test if the database contains several objects '''

        # add three objects to database
        object1 = Info(last_name='Kudrya')
        object1.save()
        object2 = Info(last_name='Kudrya')
        object2.save()
        object3 = Info(last_name='Kudrya')
        object3.save()

        info =  Info.objects.all().first()
        response = self.client.get(reverse('main'))
        self.assertTrue('info' in response.context)
        context = response.context['info']
        self.assertTrue(context.last_name == info.last_name)


class RequestsPageViewTest(TestCase):

    ''' test view for page with requests '''

    def test_requests_page_template(self):

        ''' test using template '''

        response = self.client.get(reverse('requests'))
        self.assertTemplateUsed(response, 'hello/requests.html')

    def test_requests_page(self):

        ''' test status code '''

        response = self.client.get(reverse('requests'))
        self.assertEquals(response.status_code, 200)

    def test_view_return_last_10(self):

        ''' test view return last 10 objects or less '''

        response = self.client.get(reverse('requests'))
        self.assertTrue('requests' in response.context)
        context = response.context['requests']
        self.assertTrue(len(context) <= 10)

    def test_content_requests_list(self):

        ''' test view renders required data '''

        response = self.client.get(reverse('requests'))
        self.assertTrue('requests' in response.context)
        self.assertIn('Requests',
                      response.content)
        self.assertIn('Last requests', response.content)

    def test_forajax_view_status_code(self):

        ''' test status code '''

        response = self.client.get(reverse('forajax'),
                                   content_type='application/json')
        self.assertEqual(response.status_code, 200)


    def test_forajax_view_render_data(self):

        ''' test ajax view renders required data '''

        response = self.client.get(reverse('forajax'),
                                   content_type='application/json')
        self.assertContains(response, '"status_code": "200", "method": "GET"',
                            status_code=200)
        self.assertContains(response, '"path": "/",', status_code=200)
        self.assertContains(response, '"amount":', status_code=200)
        self.assertContains(response, '"date_and_time":', status_code=200)
