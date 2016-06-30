# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.template import Template, Context


class TemplateTagTest(TestCase):

    ''' test for custom tag '''

    def test_tag_on_the_page(self):

        ''' test tag exist on the main page '''

        self.client.login(username='admin', password='admin')
        response = self.client.get(reverse('main'))
        self.assertIn('<a href="/admin/auth/user/1/">',
                      response.content)

    def test_tag_renders(self):

        ''' test tag render required url '''

        user = User.objects.first()
        template = '{% load edit_obj %} {% edit_link object %}'
        context = {'object': user}
        rendered = Template(template).render(Context(context))
        self.assertEquals(
            rendered,
            u' <a href="/admin/auth/user/1/">admin</a>'
        )

    def test_tag_accept_wrong_object(self):

        ''' test that tag does not fail if object has no attribute _meta '''

        obj = 'string'
        template = '{% load edit_obj %} {% edit_link object %}'
        context = {'object': obj}
        rendered = Template(template).render(Context(context))
        self.assertEquals(rendered,
                          u' <a href="/">string</a>')
