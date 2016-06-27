# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from django.db import models
import logging


logging.disable(logging.ERROR)


class Command(BaseCommand):
    
    def handle(self, *args, **options):
        for i in models.get_models():
            self.stdout.write(i.__name__ + ' - ' + str(i.objects.count()))
            self.stderr.write('error: ' + str(i.__name__) + ' - ' +
                              str(i.objects.count()))
