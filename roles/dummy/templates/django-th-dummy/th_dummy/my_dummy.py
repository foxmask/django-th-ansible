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
from django.utils.log import getLogger
from django.core.cache import caches

# django_th classes
from django_th.services.services import ServicesMgr


"""
{% if oauth_version %}
    handle process with {{ module_name }}
    put the following in settings.py

    TH_{{ module_name | upper }} = {
        'consumer_key': 'abcdefghijklmnopqrstuvwxyz',
        'consumer_secret': 'abcdefghijklmnopqrstuvwxyz',
    }
{% endif %}
    TH_SERVICES = (
        ...
        'th_{{ module_name }}.my_{{ module_name }}.Service{{ class_name | upper }}',
        ...
    )
"""

logger = getLogger('django_th.trigger_happy')

cache = caches['th_{{ module_name }}']


class Service{{ class_name | upper }}(ServicesMgr):
{% if oauth_version %}
    def __init__(self, token=None):
        super(Service{{ class_name | upper }}, self).__init__(token)
        self.AUTH_URL = '{{ AUTH_URL }}'
        self.ACC_TOKEN = '{{ ACC_TOKEN }}'
        self.REQ_TOKEN = '{{ REQ_TOKEN }}'
        self.consumer_key = settings.TH_{{ module_name | upper }}['consumer_key']
        self.consumer_secret = settings.TH_{{ module_name | upper }}['consumer_secret']
        if token:
            self.{{ module_name }} = {{ external_api_class }}(self.consumer_key, token)
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
        trigger_id = kwargs['trigger_id']
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
        kwargs = {}

        title, content = super(Service{{ class_name }}, self).save_data(data, **kwargs)

        if token and 'link' in data and data['link'] is not None and len(data['link']) > 0:
            # get the data of this trigger
            trigger = {{ class_name }}.objects.get(trigger_id=trigger_id)
            # if the external service need we provide
            # our stored token and token secret then I do
            # token_key, token_secret = token.split('#TH#')
            self.{{ module_name }}.add(url=data['link'], title=title, tags=(trigger.tag.lower()))

            sentence = str('{{ module_name }} {} created').format(data['link'])
            logger.debug(sentence)
            status = True
        else:
            logger.critical(
                "no token or link provided for trigger ID {} ".format(trigger_id))
            status = False
        return status

{% if oauth_version %}
    def auth(self, request):
        """
            let's auth the user to the Service
        """
        request_token = super(Service{{ class_name | upper }}, self).auth(request)
        callback_url = self.callback_url(request, 'readability')

        # URL to redirect user to, to authorize your app
        auth_url_str = '%s?oauth_token=%s&oauth_callback=%s'
        auth_url = auth_url_str % (self.AUTH_URL,
                                   request_token['oauth_token'],
                                   callback_url)

        return auth_url

    def callback(self, request):
        """
            Called from the Service when the user accept to activate it
        """
        kwargs = {'access_token': '', 'service': 'Service{{ class_name }}',
                  'return': '{{ module_name }}'}
        return super(Service{{ class_name | upper }}, self).callback(request, **kwargs)
{% endif %}