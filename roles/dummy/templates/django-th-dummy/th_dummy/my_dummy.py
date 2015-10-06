# coding: utf-8
# add here the call of any native lib of python like datetime etc.
#

# Using OAuth{{ oauth_version }}Session
from requests_oauthlib import OAuth{{ oauth_version }}Session

# add the python API here if needed
from {{ external_api }} import {{ external_api_class }}

# django classes
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.log import getLogger
from django.core.cache import caches

# django_th classes
from django_th.services.services import ServicesMgr
from django_th.models import UserService, ServicesActivated

"""
    handle process with {{ module_name }}
    put the following in settings.py

    TH_{{ module_name | upper }} = {
        'consumer_key': 'abcdefghijklmnopqrstuvwxyz',
        'consumer_secret': 'abcdefghijklmnopqrstuvwxyz',
    }

    TH_SERVICES = (
        ...
        'th_{{ module_name }}.my_{{ module_name }}.Service{{ class_name }}',
        ...
    )

"""

logger = getLogger('django_th.trigger_happy')

cache = caches['th_{{ module_name }}']


class Service{{ class_name }}(ServicesMgr):

    def __init__(self, token=None):
        self.AUTH_URL = '{{ AUTH_URL }}'
        self.ACC_TOKEN = '{{ ACC_TOKEN }}'
        self.REQ_TOKEN = '{{ REQ_TOKEN }}'
        self.consumer_key = settings.TH_{{ module_name | upper }}['consumer_key']
        self.consumer_secret = settings.TH_{{ module_name | upper }}['consumer_secret']
        if token:
            self.{{ module_name }} = {{ external_api_class }}(self.consumer_key, token)

    def read_data(self, token, trigger_id, date_triggered):
        """
            get the data from the service
            as the pocket service does not have any date
            in its API linked to the note,
            add the triggered date to the dict data
            thus the service will be triggered when data will be found
            :param trigger_id: trigger ID to process
            :param date_triggered: the date of the last trigger
            :type trigger_id: int
            :type date_triggered: datetime
            :return: list of data found from the date_triggered filter
            :rtype: list
        """
        data = list()
        cache.set('th_{{ module_name }}_' + str(trigger_id), data)

    def process_data(self, trigger_id):
        """
            get the data from the cache
            :param trigger_id: trigger ID from which to save data
            :type trigger_id: int
        """
        datas = list()
        return datas

    def save_data(self, token, trigger_id, **data):
        """
            let's save the data

            :param trigger_id: trigger ID from which to save data
            :param **data: the data to check to be used and save
            :type trigger_id: int
            :type **data:  dict
            :return: the status of the save statement
            :rtype: boolean
        """
        from th_{{ module_name }}.models import {{ class_name }}
        status = False

        if token and 'link' in data and data['link'] is not None and len(data['link']) > 0:
            # get the data of this trigger
            trigger = {{ class_name }}.objects.get(trigger_id=trigger_id)
            # if the external service need we provide
            # our stored token and token secret then I do
            # token_key, token_secret = token.split('#TH#')

                # get the token of the external service for example

            title = ''
            title = (data['title'] if 'title' in data else '')
                # add data to the external service
            item_id = self.{{ module_name }}.add(url=data['link'], title=title, tags=(trigger.tag.lower()))

            sentance = str('{{ module_name }} {} created').format(data['link'])
            logger.debug(sentance)
            status = True
        else:
            logger.critical(
                "no token or link provided for trigger ID {} ".format(trigger_id))
            status = False
        return status

    def auth(self, request):
        """
            let's auth the user to the Service
        """
        callback_url = 'http://%s%s' % (
            request.get_host(), reverse('{{ module_name }}_callback'))

        request_token = self.get_request_token()

        # Save the request token information for later
        request.session['oauth_token'] = request_token['oauth_token']
        request.session['oauth_token_secret'] = request_token[
            'oauth_token_secret']

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

        try:
            # finally we save the user auth token
            # As we already stored the object ServicesActivated
            # from the UserServiceCreateView now we update the same
            # object to the database so :
            # 1) we get the previous objet
            us = UserService.objects.get(
                user=request.user,
                name=ServicesActivated.objects.get(name='Service{{ class_name }}'))
            # 2) Readability API require to use 4 parms consumer_key/secret +
            # token_key/secret instead of usually get just the token
            # from an access_token request. So we need to add a string
            # seperator for later use to slpit on this one
            access_token = self.get_access_token(
                request.session['oauth_token'],
                request.session['oauth_token_secret'],
                request.GET.get('oauth_verifier', '')
            )
            # us.token = access_token.get('oauth_token') + \
            #    '#TH#' + access_token.get('oauth_token_secret')
            us.token = access_token
            # 3) and save everything
            us.save()
        except KeyError:
            return '/'

        return '{{ module_name }}/callback.html'

    def get_request_token(self):
        oauth = OAuth{{ oauth_version }}Session(self.consumer_key,
                              client_secret=self.consumer_secret)
        return oauth.fetch_request_token(self.REQ_TOKEN)

    def get_access_token(self, oauth_token, oauth_token_secret,
                         oauth_verifier):
        # Using OAuth1Session
        oauth = OAuth{{ oauth_version }}Session(self.consumer_key,
                              client_secret=self.consumer_secret,
                              resource_owner_key=oauth_token,
                              resource_owner_secret=oauth_token_secret,
                              verifier=oauth_verifier)
        oauth_tokens = oauth.fetch_access_token(self.ACC_TOKEN)

        return oauth_tokens
