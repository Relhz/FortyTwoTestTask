from django.test import LiveServerTestCase
from selenium import webdriver
from django.test import TestCase
from django.core.urlresolvers import reverse
from models import Info


class MainPageSeleniumTest(LiveServerTestCase):

    ''' simulate users behaviour '''

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_main_page(self):

        ''' users actions '''

        # user enter into the main page
        self.browser.get(self.live_server_url)

        # user sees a header '42 test...'
        body = self.browser.find_element_by_tag_name('body').text
        self.assertIn('42 Coffee Cups Test Assignment', body)

        # user sees person info table
        info = self.browser.find_elements_by_tag_name('td')
        self.assertIn('Name', info[0].text)
        self.assertIn('Contacts', info[2].text)


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
        # old assertions which we don't need anymore
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
