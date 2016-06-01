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
        self.assertTrue('info' in response.context)

    def test_render_all_fields(self):

        ''' test does all fields render '''

        response = self.client.get(reverse('main'))
        context = response.context['info']
        self.assertTrue(context.name == 'Yevhen')
        self.assertTrue(context.last_name == 'Kudrya')
        self.assertTrue(str(context.date_of_birth) == '1990-01-21')
        self.assertTrue(context.bio == 'Information Information Information' +
                        ' Information Information Information Information')
        self.assertTrue(context.contacts == '0502455842')
        self.assertTrue(context.email == 'yevhenkudrya@gmail.com')
        self.assertTrue(context.jabber == 'relhz@42cc.co')
        self.assertTrue(context.other_contacts == 'contacts contacts ' +
                        'contacts contacts contacts')
        self.assertTrue(context.skype == 'seekandstrike')

    def test_render_cyrillic(self):

        ''' test does cyrillic symbols render'''

        info = Info.objects.get(last_name='Kudrya')
        info.name = 'Євген'
        info.save()
        response = self.client.get(reverse('main'))
        context = response.context['info']
        self.assertEquals(response.status_code, 200)
        self.assertTrue(context.name == u'Євген')

    def test_get_or_create(self):

        ''' test if object doesn't exist '''

        info = Info.objects.all()
        for i in info:
            i.delete()
            i.save
        response = self.client.get(reverse('main'))
        context = response.context['info']
        self.assertEquals(response.status_code, 200)
        self.assertTrue(context.last_name == 'Kudrya')
        self.assertTrue(context.name == None)

    def test_several_objects(self):

        ''' test if database contains several objects '''

        object1 = Info(last_name='Kudrya')
        object1.save()
        object2 = Info(last_name='Kudrya')
        object2.save()
        object3 = Info(last_name='Kudrya')
        object3.save()
        response = self.client.get(reverse('main'))
        context = response.context['info']
        self.assertEquals(response.status_code, 200)
        self.assertTrue(context.last_name == 'Kudrya')


class ModelTest(TestCase):

    ''' testing model '''

    def test_model_create(self):

        ''' test model create successfuly '''

        info = Info(last_name='Pythonenko')
        info.save()
        inf = Info.objects.all().last()
        self.assertEquals(inf, info)

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
