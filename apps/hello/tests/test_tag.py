# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse
from apps.hello.models import Info
from django.template import Template, Context


class TemplateTagTest(TestCase):

    ''' test for custom tag '''

    def test_tag_on_the_page(self):

        ''' test tag exist on the main page '''

        self.client.login(username='admin', password='admin')
        response = self.client.get(reverse('main'))
        self.assertIn('/admin/hello/info/1/', response.content)

    def test_tag_renders(self):

        ''' test tag render required url '''

        info = Info.objects.first()
        template = '{% load edit_obj %} {% into_admin object %}'
        context = {'object': info}
        rendered = Template(template).render(Context(context))
        self.assertEquals(rendered, u' /admin/hello/info/1/')
