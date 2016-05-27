from django.test import LiveServerTestCase
from django.test import TestCase
from django.core.urlresolvers import reverse
from models import Info
from models import Requests
from django.contrib.auth.models import User


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
        context = response.context['info']

        # old assertions which we don't need anymore because now we use
        # info object, not info dict
        # self.assertIn('Last name', context.keys())
        # self.assertIn('Email', context.keys())


class ModelTest(TestCase):

    ''' testing model '''

    def test_model_create(self):

        ''' test model create successfuly '''

        info = Info(last_name='Pythonenko')
        info.save()
        inf = Info.objects.all()
        self.assertEquals(inf[0], info)

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
        self.assertEquals(info.email, 'qkerbv@i.ua')
        self.assertEquals(info.bio, 'information information information')


class RequestsPageViewTest(TestCase):

    ''' test view for page with requests '''

    def test_requests_page_template(self):

        ''' test using template '''

        for i in range(32):
            self.client.get(reverse('main'))
        response = self.client.get(reverse('requests'))
        self.assertTemplateUsed(response, 'hello/requests.html')

    def test_requests_page(self):

        ''' test status code '''

        for i in range(32):
            self.client.get(reverse('main'))
        response = self.client.get(reverse('requests'))
        self.assertEquals(response.status_code, 200)

    def test_content_requests_list(self):

        ''' test view renders required data '''

        for i in range(32):
            self.client.get(reverse('main'))
        response = self.client.get(reverse('requests'))
        self.assertIn('Requests',
                      response.content)
        self.assertIn('Last requests', response.content)
        self.assertTrue('requests' in response.context)


class MiddlewareTest(TestCase):

    ''' test middleware '''

    def test_middleware_records(self):

        ''' test middleware make record to the database '''

        before_request = Requests.objects.all().count()
        self.client.get(reverse('main'))
        after_request = Requests.objects.all().count()
        self.assertTrue(before_request < after_request)

    def test_middleware_right_data(self):

        ''' test middleware make record with right data'''

        self.client.get('some_url')
        after_request = Requests.objects.all().last()
        self.assertIn('some_url', after_request.path)
        self.assertEquals('GET', after_request.method)
        self.assertEquals(unicode('404'), after_request.status_code)
        

    def test_middleware_max_records(self):

        ''' test deleting old records from db if its amount equal 30 '''

        for i in range(35):
            self.client.get(reverse('main'))
        self.assertEqual(Requests.objects.all().count(), 30)
        request = Requests.objects.all().first()
        self.client.get(reverse('requests'))
        after_request = Requests.objects.all().first()
        self.assertTrue(request != after_request)




