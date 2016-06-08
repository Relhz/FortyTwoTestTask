# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse
from apps.hello.models import Info, Requests


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
        object1 = Info(last_name='First')
        object1.save()
        object2 = Info(last_name='Second')
        object2.save()
        object3 = Info(last_name='Third')
        object3.save()

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

        for i in range(15):
            response = self.client.get(reverse('requests'))
        self.assertIn('requests', response.context)
        context = response.context['requests']
        objects = Requests.objects.all().order_by('-pk')[:10]
        self.assertEqual(len(context), 10)
        self.assertEqual(context[9], objects[9])
        self.assertEqual(context[0], objects[0])

    def test_content_requests_list(self):

        ''' test view renders required data '''

        response = self.client.get(reverse('requests'))
        self.assertIn('requests', response.context)
        self.assertIn('Requests',
                      response.content)
        self.assertIn('Last requests', response.content)

    def test_forajax_view_status_code(self):

        ''' test status code '''

        response = self.client.get(reverse('forajax'),
                                   content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_forajax_view_render_correct_data(self):

        ''' test ajax view renders required data '''

        for i in range(15):
            response = self.client.get(reverse('requests'))
        response = self.client.get(reverse('forajax'),
                                   content_type='application/json')
        request = Requests.objects.last()
        self.assertContains(response, request.path, count=10)
        self.assertContains(response, request.method, count=10)
        self.assertContains(response, request.date_and_time.isoformat()[:19],
                            count=10)
