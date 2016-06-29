# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from django.db import models
import logging
from optparse import make_option


class Command(BaseCommand):

    option_list = BaseCommand.option_list + (
        make_option(
            '--loglevel',
            action='store',
            default=False,
            help='logging level'
        ),
    )

    def handle(self, *args, **options):

        logger = logging.getLogger(__name__)

        if options['loglevel']:
            lvl = options['loglevel']
            numeric_lvl = getattr(logging, lvl.upper(), None)
            # raise ValueError in case of incorrect loglevel value
            if not isinstance(numeric_lvl, int):
                raise ValueError('Invalid log level: %s' % lvl)

            logging.basicConfig(level=numeric_lvl)
            logging.disable(numeric_lvl - 10)
            logger.debug(lvl)
            self.stdout.write('logging level - {0}'.format(numeric_lvl))
        else:
            # disable DEBUG logs by default
            logging.disable(logging.DEBUG)

        for i in models.get_models():
            self.stdout.write(i.__name__ + ' - ' + str(i.objects.count()))
            self.stderr.write('error: ' + str(i.__name__) + ' - ' +
                              str(i.objects.count()))
