# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate


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


class EditFormTest(TestCase):

    ''' test edit form  '''

    def test_login_required(self):

        ''' test unable edit data if user non authenticated '''

        response = self.client.post(reverse('forajax_edit'))
        self.assertEqual(response.status_code, 302)

    def test_edit_post(self):

        ''' send post data '''

        self.client.login(username='admin', password='admin')
        response = self.client.post(reverse('forajax_edit'),
                   {'Name': 'newName', 'Last_name': 'newSurname',
                   'Date_of_birst': '1996-2-29', 'Contacts': '',
                   'Email': '', 'Skype': '', 'Jabber': '',
                   'Other_contacts': '', 'Bio': ''})
        self.assertEqual(response.status_code, 200)
