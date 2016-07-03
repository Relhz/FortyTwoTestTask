# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse
from apps.hello.models import Requests


class LoginFormTest(TestCase):

    ''' test login form '''

    def test_login(self):

        ''' try to login '''

        response = self.client.post(
            reverse('login'),
            {'username': 'admin', 'password': 'admin'}
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

        response = self.client.post(reverse('edit', args=[1]))
        self.assertEqual(response.status_code, 302)

    def test_edit_post(self):

        ''' send post data '''

        self.client.login(username='admin', password='admin')
        response = self.client.post(
            reverse('edit', args=[1]),
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
            reverse('edit', args=[1]),
            {'name': '@@@@@@@$$$$$$', 'last_name': '$$$$$$###'}
        )
        self.assertIn('"name": ["Please, write only ', response.content)
        self.assertIn('"last_name": ["Please, write only ', response.content)

    def test_form_action_url(self):

        ''' test form action attribute contains required url '''

        self.client.login(username='admin', password='admin')
        response = self.client.get(reverse('edit', args=[1]))
        self.assertIn(reverse('edit', args=[1]), response.content)


class PriorityFormTest(TestCase):

    ''' test priority form '''

    def test_page_contains_form(self):

        ''' test page contains required priority forms '''

        Requests.objects.bulk_create(Requests() for i in range(10))
        response = self.client.get(reverse('requests'))
        self.assertContains(response, reverse('requests'), count=11)
        self.assertContains(response, '<input id="id_priority"', count=10)

    def test_requests_initial(self):

        ''' test form for priority editing contains initial data '''

        Requests.objects.bulk_create(
            Requests(priority=888) for i in range(10))
        response = self.client.get(reverse('requests'))
        self.assertContains(response, 'value="888"', 9)

    def test_priority_form__post(self):

        ''' send post data to priority form '''

        self.client.login(username='admin', password='admin')
        obj_id = Requests.objects.last().id
        response = self.client.post(
            reverse('requests', args=[obj_id]), {'priority': 33}
        )
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('requests'))
        print response
        self.assertContains(response, 'value="33"', 1)
