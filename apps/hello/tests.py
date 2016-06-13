# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse
from models import Info


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
        self.assertIn('<h1>42 Coffee Cups Test Assignment</h1>',
                      response.content)
        self.assertIn('Skype', response.content)
        self.assertIn('info', response.context)

    def test_render_all_fields(self):

        ''' test does all fields render '''

        response = self.client.get(reverse('main'))
        info = Info.objects.get(last_name='Kudrya')

        self.assertEqual(response.context['info'], info)

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
        self.assertIn('info', response.context)
        self.assertContains(response, 'Database is empty', count=1,
                            status_code=200)

    def test_if_several_objects_in_db(self):

        ''' test if the database contains several objects '''

        Info.objects.all().delete()
        # add three objects to database
        Info.objects.bulk_create([
            Info(last_name='First'),
            Info(last_name='Second'),
            Info(last_name='Third')
        ])

        info = Info.objects.all().first()
        response = self.client.get(reverse('main'))
        self.assertIn('info', response.context)
        self.assertEqual(response.context['info'], info)
        self.assertContains(response, 'First', count=1, status_code=200)


class ModelTest(TestCase):

    ''' testing model '''

    def test_unicode_method(self):

        ''' test model object represents as string '''

        info = Info(last_name='Pythonenko')
        self.assertEqual(str(info), info.last_name)

    def test_model_fields(self):

        ''' test model fields '''

        info = Info(last_name='Pythonenko')
        info.save()
        self.assertEquals(info.last_name, 'Pythonenko')
        self.assertTrue(hasattr(info, 'name'))
        self.assertTrue(hasattr(info, 'bio'))
        self.assertTrue(hasattr(info, 'jabber'))
        info.date_of_birst = '1995-03-03'
        info.email = 'qkerbv@i.ua'
        info.bio = 'information information information'
        info.save()
        self.assertEquals(info.date_of_birst, '1995-03-03')


class AdminSiteTest(TestCase):

    ''' testing the admin site '''

    def test_home_page(self):

        ''' test status code '''

        response = self.client.get('/admin/')
        self.assertEquals(response.status_code, 200)

    def test_login_admin(self):

        ''' test if admin can log-in '''

        response = self.client.post(
            '/admin/',
            {'name': 'admin', 'password': 'admin via fixtures'}
        )
        self.assertEquals(response.status_code, 200)

    def test_contains_required_data(self):

        ''' test that admin page contains required data '''

        self.client.login(username='admin', password='admin via fixtures')
        response = self.client.get('/admin/hello/info/')
        info = Info.objects.first().last_name
        self.assertIn(info, response.content)
