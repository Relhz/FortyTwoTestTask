from django.test import TestCase
from apps.hello.models import Info


class AdminSiteTest(TestCase):

    ''' testing the admin site '''

    def test_home_page(self):

        ''' test status code '''

        response = self.client.get('/admin/')
        self.assertEquals(response.status_code, 200)

    def test_login_admin(self):

        ''' test if admin can log-in '''

        response = self.client.post(
            '/admin/',
            {'name': 'admin', 'password': 'admin via fixtures'}
        )
        self.assertEquals(response.status_code, 200)

    def test_contains_required_data(self):

        ''' test that admin page contains required data '''

        self.client.login(username='admin', password='admin')
        response = self.client.get('/admin/hello/info/')
        info = Info.objects.first().last_name
        self.assertIn(info, response.content)
