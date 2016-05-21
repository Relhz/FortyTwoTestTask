from django.test import LiveServerTestCase
from selenium import webdriver


class MainPageSeleniumTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_main_page(self):

        #user enter into the main page
        self.browser.get(self.live_server_url)

        #user sees a header '42 test...'
        body = self.browser.find_element_by_tag_name('body').text
        self.assertIn('42 Coffee Cups Test Assignment', body)

        #user sees person info table
        info = self.browser.find_elements_by_tag_name('td')
        for i in info:
            self.assertIn('Name', i.text)
            self.assertIn('Contacts', i.text)



