from django.core.management import call_command
from django.test import TestCase
from django.utils.six import StringIO
from django.db import models


class CustomCommandTest(TestCase):

    ''' test custom command '''

    def test_command(self):

        " test output contains models and amount of objects "

        stderr = StringIO()
        stdout = StringIO()
        first_model = models.get_models()[0]
        last_model = models.get_models()[-1]
        call_command('allmodels', stdout=stdout, stderr=stderr)
        # first model and amount of its objects are in the stdout and stderr
        self.assertIn(first_model.__name__, stdout.getvalue())
        self.assertIn(str(first_model.objects.count()), stdout.getvalue())
        self.assertIn(first_model.__name__, stderr.getvalue())
        self.assertIn(str(first_model.objects.count()), stderr.getvalue())
        # last model and amount of objects its are in the stdout and stderr
        self.assertIn(last_model.__name__, stdout.getvalue())
        self.assertIn(str(last_model.objects.count()), stdout.getvalue())
        self.assertIn(last_model.__name__, stderr.getvalue())
        self.assertIn(str(last_model.objects.count()), stderr.getvalue())
