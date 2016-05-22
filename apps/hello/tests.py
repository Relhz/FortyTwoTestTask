from django.test import LiveServerTestCase
from selenium import webdriver
from django.test import TestCase
from django.core.urlresolvers import reverse
from models import Info
from models import Requests
from django.contrib.auth.models import User


class MainPageSeleniumTest(LiveServerTestCase):

    ''' simulate users behaviour '''

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_main_page(self):

        ''' users actions on main page'''

        # user enter into the main page
        self.browser.get(self.live_server_url)

        # user sees a header '42 test...'
        body = self.browser.find_element_by_tag_name('body').text
        self.assertIn('42 Coffee Cups Test Assignment', body)

        # user sees person info table
        info = self.browser.find_elements_by_tag_name('td')
        self.assertIn('Name', info[0].text)
        self.assertIn('Contacts', info[2].text)

    def test_reguests_page(self):

        ''' users actions on page with requests'''

        # user enter into the page
        self.browser.get(self.live_server_url + '/requests/')

        # user sees a header 'Requests'
        body = self.browser.find_element_by_tag_name('body').text
        self.assertIn('Requests', body)

        # user sees list of requests
        list_requests = self.browser.find_elements_by_tag_name('p')
        self.assertIn('Last requests:', list_requests[0].text)
        self.assertTrue(len(list_requests) == 11)


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

        self.assertTrue(hasattr(context, 'last_name'))
        self.assertTrue(hasattr(context, 'email'))


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

        response = self.client.get(reverse('requests'))
        self.assertTemplateUsed(response, 'hello/requests.html')

    def test_requests_page(self):

        ''' test status code '''

        response = self.client.get(reverse('requests'))
        self.assertEquals(response.status_code, 200)

    def test_content_requests_list(self):

        ''' test view renders required data '''

        response = self.client.get(reverse('requests'))
        self.assertIn('<h1>Requests</h1>',
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
        print after_request
        self.assertIn('some_url', after_request.path)
        self.assertEquals('GET', after_request.method)
        self.assertEquals(unicode('404'), after_request.status_code)
        

    def test_middleware_max_records(self):

        ''' test deleting old records from db if its amount equal 30 '''

        for i in range(32):
            self.client.get(reverse('requests'))
        self.assertEqual(Requests.objects.all().count(), 30)
        request = Requests.objects.all().first()
        self.client.get(reverse('requests'))
        after_request = Requests.objects.all().first()
        self.assertTrue(request != after_request)




