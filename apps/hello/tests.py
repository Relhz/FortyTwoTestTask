from django.test import LiveServerTestCase
from selenium import webdriver
from django.test import TestCase
from django.core.urlresolvers import resolve
from django.core.urlresolvers import reverse
from . import views


'''class MainPageSeleniumTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_main_page(self):

        # user enter into the main page
        self.browser.get(self.live_server_url)

        # user sees a header '42 test...'
        body = self.browser.find_element_by_tag_name('body').text
        self.assertIn('42 Coffee Cups Test Assignment', body)

        # user sees person info table
        info = self.browser.find_elements_by_tag_name('td')
        for i in info:
            self.assertIn('Name', i.text)
            self.assertIn('Contacts', i.text)'''


class MainPageViewTest(TestCase):

    # test used view
    def test_root_url_view(self):
        rooturl = resolve(reverse('main'))
        self.assertEquals(rooturl.func, views.main)

    # test using template
    def test_root_url_template(self):
        response = self.client.get(reverse('main'))
        self.assertTemplateUsed(response, 'base.html')
      
    # test status code
    def test_main_page(self):
        response = self.client.get(reverse('main'))
        self.assertEquals(response.status_code, 200)

    # test view renders required data
    def test_content_info(self):
        response = self.client.get(reverse('main'))
        self.assertIn('<h1>42 Coffee Cups Test Assignment</h1>', response.content)
        self.assertIn('Skype', response.content)
        self.assertTrue('info' in response.context)
        context = response.context['info']
        self.assertIn('Last name', context.keys())
        self.assertIn('Email', context.keys())



