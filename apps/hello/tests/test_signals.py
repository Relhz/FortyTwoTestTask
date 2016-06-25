# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse
from apps.hello.models import Info, ModelsAction


class SignalsTest(TestCase):

    ''' test signals work '''

    def test_signal_create(self):

    	''' test append the record into db if new object created '''

    	Info.objects.create(last_name='nEwAweSoMESUrname')
    	self.assertEqual(ModelsAction.objects.last().modelname, Info.__name__)
    	self.assertEqual(ModelsAction.objects.last().action, 'create')

    def test_signal_edit(self):

    	''' test append the record into db if object edited '''

    	Info.objects.create(last_name='nEwAweSoMESUrname')
    	info = Info.objects.last()
    	info.skype = 'lolskype'
    	info.save()
    	self.assertEqual(ModelsAction.objects.last().modelname, Info.__name__)
    	self.assertEqual(ModelsAction.objects.last().action, 'edit')

    def test_signal_delete(self):

    	''' test append the record into db if object deleted '''

    	Info.objects.create(last_name='nEwAweSoMESUrname')
    	Info.objects.last().delete()
    	self.assertEqual(ModelsAction.objects.last().modelname, Info.__name__)
    	self.assertEqual(ModelsAction.objects.last().action, 'delete')
