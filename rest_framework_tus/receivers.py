# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging

from django.dispatch import receiver

from rest_framework_tus.models import get_upload_model
from rest_framework_tus.signals import received, saved, finished
from rest_framework_tus.storage import get_save_handler

logger = logging.getLogger(__name__)


@receiver(received)
def on_receiving_done(sender, instance, **kwargs):
    if not issubclass(sender, get_upload_model()):
        return
    logger.debug('on_receiving_done: {}'.format(instance))
    save_handler = get_save_handler()
    save_handler(upload=instance).run()


@receiver(saved)
def on_saving_done(sender, instance, **kwargs):
    if not issubclass(sender, get_upload_model()):
        return
    logger.debug('on_saving_done: {}'.format(instance))


@receiver(finished)
def on_finished(sender, instance, **kwargs):
    if not issubclass(sender, get_upload_model()):
        return
    logger.debug('on_finished: {}'.format(instance))
