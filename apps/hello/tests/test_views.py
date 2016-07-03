# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse
from apps.hello.models import Info, Requests
from django.utils import timezone


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
        self.assertIn('42 Coffee Cups Test Assignment',
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

    def test_view_return_last_10(self):

        ''' test view return last 10 objects '''

        Requests.objects.bulk_create(
            Requests(path='/response/', method='GET',
                     requests_date_time=timezone.now()) for i in range(15)
            )
        response = self.client.get(reverse('requests'))
        self.assertIn('objects', response.context)
        context = response.context['objects']
        objects = Requests.objects.all().order_by('-pk')[:10]
        self.assertEqual(len(context), 10)
        self.assertEqual(list(context), list(objects))

    def test_content_requests_list(self):

        ''' test view renders required data '''

        response = self.client.get(reverse('requests'))
        self.assertIn('objects', response.context)
        self.assertIn('Requests',
                      response.content)
        self.assertIn('Last requests', response.content)

    def test_view_render_correct_data(self):

        ''' test view renders required data after ajax request '''

        Requests.objects.bulk_create(
            Requests(path=reverse('login'), method='GET',
                     requests_date_time=timezone.now()) for i in range(15)
            )
        objects = Requests.objects.last()
        response = self.client.get(reverse('requests'),
                                   content_type='application/json')
        self.assertContains(response, objects.path, count=9)
        self.assertContains(response, objects.method, count=10)
        self.assertContains(
            response,
            objects.requests_date_time.isoformat()[:10], count=10
        )

    def test_priority_form_errors(self):

        ''' check requests view returns priority form errors '''

        self.client.login(username='admin', password='admin')
        response = self.client.post(reverse('requests', args=[1]),
                                    {'priority': 0.01})
        self.assertIn('"priority": ["Enter a whole number."]',
                      response.content)


class LoginViewTest(TestCase):

    ''' test login view  '''

    def test_login_template(self):

        ''' test using template '''

        response = self.client.get(reverse('login'))
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_login_page(self):

        ''' test status code '''

        response = self.client.get(reverse('login'))
        self.assertEquals(response.status_code, 200)

    def test_login_content(self):

        ''' test view renders required data '''

        response = self.client.get(reverse('login'))
        self.assertIn('Username', response.content)
        self.assertIn('Password', response.content)
        self.assertIn('form', response.context)

    def test_user_already_logged_in(self):

        ''' test show message if user already logged in'''

        self.client.login(username='admin', password='admin')
        response = self.client.get(reverse('login'))
        self.assertContains(response, 'You are already logged in', count=1,
                            status_code=200)

    def test_login_redirects(self):

        ''' test login view redirects to edit page or login page'''

        response = self.client.post(reverse('login'),
                                    {'username': 'admin',
                                     'password': 'admin'})
        self.assertRedirects(response, reverse('edit', args=[1]))

    def test_logout_redirects(self):

        ''' test logout view redirects to the main page '''

        response = self.client.post(reverse('logout'))
        self.assertRedirects(response, reverse('main'))


class EditViewTest(TestCase):

    ''' test edit view  '''

    def test_edit_template(self):

        ''' test using template '''

        self.client.login(username='admin', password='admin')
        response = self.client.get(reverse('edit', args=[1]))
        self.assertTemplateUsed(response, 'hello/edit.html')

    def test_edit_page(self):

        ''' test status code '''

        self.client.login(username='admin', password='admin')
        response = self.client.get(reverse('edit', args=[1]))
        self.assertEquals(response.status_code, 200)

    def test_edit_content(self):

        ''' test view renders required data '''

        self.client.login(username='admin', password='admin')
        response = self.client.get(reverse('edit', args=[1]))
        self.assertIn('form', response.context)
        self.assertIn('Name', response.content)
        self.assertIn('Last name', response.content)
        self.assertIn('Date of birth', response.content)
        self.assertIn('Photo', response.content)
        self.assertIn('Contacts', response.content)
        self.assertIn('Email', response.content)
        self.assertIn('Skype', response.content)
        self.assertIn('Jabber', response.content)
        self.assertIn('Other contacts:', response.content)
        self.assertIn('Bio', response.content)

    def test_edit_initial(self):

        ''' test form contains initial data '''

        self.client.login(username='admin', password='admin')
        response = self.client.get(reverse('edit', args=[1]))
        info = Info.objects.first()
        self.assertIn(info.name, response.content)
        self.assertIn(info.last_name, response.content)
        self.assertIn(info.date_of_birth.isoformat()[:10], response.content)
        self.assertIn(info.photo.url, response.content)
        self.assertIn(info.contacts, response.content)
        self.assertIn(info.email, response.content)
        self.assertIn(info.skype, response.content)
        self.assertIn(info.jabber, response.content)
        self.assertIn(info.other_contacts, response.content)
        self.assertIn(info.bio, response.content)

    def test_return_form_errors(self):

        ''' check view returns form errors after request with wrong data '''

        self.client.login(username='admin', password='admin')
        response = self.client.post(reverse('edit', args=[1]),
                                    {'date_of_birth': '1990-13-55'})
        self.assertIn('"date_of_birth": ["Enter a valid date."]',
                      response.content)
        self.assertIn('"last_name": ["This field is required."]',
                      response.content)
