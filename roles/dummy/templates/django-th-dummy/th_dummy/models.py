# coding: utf-8
from django.db import models
from django_th.models.services import Services
from django_th.models import TriggerService


class {{ class_name }}(Services):

    """
        {{ module_name }} model to be adapted for the new service
    """
    # put whatever you need  here
    # eg title = models.CharField(max_length=80)
    # but keep at least this one
    trigger = models.ForeignKey(TriggerService)

    class Meta:
        app_label = 'th_{{ module_name }}'
        db_table = 'django_th_{{ module_name }}'

    def __str__(self):
        return self.name

    def show(self):
        return "My {{ class_name }} %s" % self.name
