# coding: utf-8
# add here the call of any native lib of python like datetime etc.

{% if external_api %}
# add the python API here if needed
from {{ external_api }} import {{ external_api_class }}
{% endif %}
# django classes
{% if oauth_version %}
from django.conf import settings
{% endif %}
from django.core.cache import caches

from logging import getLogger

# django_th classes
from django_th.services.services import ServicesMgr


"""
{% if oauth_version %}
    handle process with {{ module_name }}
    put the following in th_settings.py

    TH_{{ module_name | upper }} = {
        'consumer_key': 'abcdefghijklmnopqrstuvwxyz',
        'consumer_secret': 'abcdefghijklmnopqrstuvwxyz',
    }
{% endif %}
    TH_SERVICES = (
        ...
        'th_{{ module_name }}.my_{{ module_name }}.Service{{ class_name }}',
        ...
    )
"""

logger = getLogger('django_th.trigger_happy')

cache = caches['th_{{ module_name }}']


class Service{{ class_name }}(ServicesMgr):

{% if oauth_version %}
    def __init__(self, token=None):
        super(Service{{ class_name }}, self).__init__(token)
        self.AUTH_URL = '{{ AUTH_URL }}'
        self.ACC_TOKEN = '{{ ACC_TOKEN }}'
        self.REQ_TOKEN = '{{ REQ_TOKEN }}'
        self.consumer_key = settings.TH_{{ module_name | upper }}['consumer_key']
        self.consumer_secret = settings.TH_{{ module_name | upper }}['consumer_secret']
        self.token = token
        self.service = 'Service{{ class_name }}'
        self.oauth = '{{ oauth_version }}'
        if token:
            self.{{ module_name }} = {{ external_api_class }}(self.consumer_key, self.consumer_secret, token)

{% endif %}
    def read_data(self, **kwargs):
        """
            get the data from the service
            as the pocket service does not have any date
            in its API linked to the note,
            add the triggered date to the dict data
            thus the service will be triggered when data will be found

            :param kwargs: contain keyword args : trigger_id at least
            :type kwargs: dict

            :rtype: list
        """
        trigger_id = kwargs.get('trigger_id')
        data = list()
        cache.set('th_{{ module_name }}_' + str(trigger_id), data)

    def save_data(self, trigger_id, **data):
        """
            let's save the data
            :param trigger_id: trigger ID from which to save data
            :param data: the data to check to be used and save
            :type trigger_id: int
            :type data:  dict
            :return: the status of the save statement
            :rtype: boolean
        """
        from th_{{ module_name }}.models import {{ class_name }}

        status = False

        title, content = super(Service{{ class_name }}, self).save_data(trigger_id, **data)

        # get the data of this trigger
        trigger = {{ class_name }}.objects.get(trigger_id=trigger_id)
        # we suppose we use a tag property for this service
        status = self.{{ module_name }}.add(title=title, content=content, tags= trigger.tags)

        return status

