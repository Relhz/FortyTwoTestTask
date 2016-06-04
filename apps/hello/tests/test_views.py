# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse
from apps.hello.models import Info


class MainPageViewTest(TestCase):

    ''' testing view for main page '''

    def test_root_url_template(self):

        ''' test using template '''

        response = self.client.get(reverse('main'))
        self.assertTemplateUsed(response, 'hello/main.html')

    def test_main_page(self):

        ''' test status code '''

        response = self.client.get(reverse('main'))
        self.assertEquals(response.status_code, 200)

    def test_content_info(self):

        ''' test view renders required data '''

        response = self.client.get(reverse('main'))
        self.assertIn('<h1><a href="/">42 Coffee Cups Test Assignment</a>' +
                      '</h1>', response.content)
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

        Info.objects.all().delete()

        response = self.client.get(reverse('main'))
        self.assertTrue('message' in response.context)
        context = response.context['message']
        self.assertTrue(context == 'Database is empty')
        self.assertContains(response, 'Database is empty', count=1,
                            status_code=200)

    def test_if_several_objects_in_db(self):

        ''' test if the database contains several objects '''

        Info.objects.all().delete()
        # add three objects to database
        object1 = Info(last_name='First')
        object1.save()
        object2 = Info(last_name='Second')
        object2.save()
        object3 = Info(last_name='Third')
        object3.save()

        info =  Info.objects.all().first()
        response = self.client.get(reverse('main'))
        self.assertTrue('info' in response.context)
        self.assertTrue(response.context['info'].last_name == info.last_name)
        self.assertContains(response, 'First', count=1, status_code=200)


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


class LoginViewTest(TestCase):

    ''' test login view  '''

    def test_login_template(self):

        ''' test using template '''

        response = self.client.get(reverse('login'))
        self.assertTemplateUsed(response, 'hello/login.html')

    def test_login_page(self):

        ''' test status code '''

        response = self.client.get(reverse('login'))
        self.assertEquals(response.status_code, 200)

    def test_login_content(self):

        ''' test view renders required data '''

        response = self.client.get(reverse('login'))
        self.assertIn('Username', response.content)
        self.assertIn('Password', response.content)
        self.assertTrue('form' in response.context)


class EditViewTest(TestCase):

    ''' test edit view  '''

    def test_edit_template(self):

        ''' test using template '''

        response = self.client.get(reverse('edit'))
        self.assertTemplateUsed(response, 'hello/edit.html')

    def test_edit_page(self):

        ''' test status code '''

        response = self.client.get(reverse('edit'))
        self.assertEquals(response.status_code, 200)

    def test_edit_content(self):

        ''' test view renders required data '''

        response = self.client.get(reverse('edit'))
        self.assertIn('Last name',
                      response.content)
        self.assertIn('Other contacts:', response.content)
        self.assertTrue('form' in response.context)
        self.assertTrue('loginform' in response.context)
