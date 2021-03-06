from apps.hello.models import ModelsAction
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
import logging
from fortytwo_test_task.settings.common import IGNORED_SIGNALS


logger = logging.getLogger(__name__)


@receiver(post_save, dispatch_uid='uid')
def post_save_signal(sender, created, **kwargs):
    logger.debug('sender >>>>>>>>>> ' + str(sender))
    if created and sender.__name__ not in IGNORED_SIGNALS:
        ModelsAction.objects.create(modelname=sender.__name__,
                                    action='Create')
    elif sender.__name__ not in IGNORED_SIGNALS:
        ModelsAction.objects.create(modelname=sender.__name__, action='Edit')


@receiver(post_delete, dispatch_uid='uid')
def post_delete_signal(sender, **kwargs):
    logger.debug('sender >>>>>>>>>> ' + str(sender))
    if sender.__name__ not in IGNORED_SIGNALS:
        ModelsAction.objects.create(modelname=sender.__name__,
                                    action='Delete')
