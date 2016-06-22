# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse


class LoginFormTest(TestCase):

    ''' test login form '''

    def test_login(self):

        ''' try to login '''

        response = self.client.post(
            reverse('log_in'),
            {'Username': 'admin', 'Password': 'admin'}
        )
        self.assertEqual(response.status_code, 302)

    def test_logout(self):

        ''' try to logout '''

        response = self.client.post(reverse('logout'))
        self.assertEqual(response.status_code, 302)


class EditFormTest(TestCase):

    ''' test edit form  '''

    def test_login_required(self):

        ''' test unable edit data if user non authenticated '''

        response = self.client.post(reverse('edit'))
        self.assertEqual(response.status_code, 302)

    def test_edit_post(self):

        ''' send post data '''

        self.client.login(username='admin', password='admin')
        response = self.client.post(
            reverse('edit'),
            {'name': 'newName', 'last_name': 'newSurname',
             'date_of_birth': '1996-2-29', 'contacts': '',
             'email': '', 'skype': '', 'jabber': '',
             'other_contacts': '', 'bio': ''}
        )
        self.assertEqual(response.status_code, 200)

    def test_edit_form_validators(self):

        ''' test validation error returns '''

        self.client.login(username='admin', password='admin')
        response = self.client.post(
            reverse('edit'),
            {'name': '@@@@@@@$$$$$$', 'last_name': '$$$$$$###'}
        )
        self.assertIn('"name": ["Please, write only ', response.content)
        self.assertIn('"last_name": ["Please, write only ', response.content)
