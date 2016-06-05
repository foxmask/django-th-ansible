# coding: utf-8
from django.test import TestCase
from django.conf import settings
from django.contrib.auth.models import User
from th_{{ module_name }}.models import {{ class_name | upper }}
from django_th.models import TriggerService, UserService, ServicesActivated
from th_{{ module_name }}.forms import {{ class_name | upper }}ProviderForm, {{ class_name | upper }}ConsumerForm


class {{ class_name | upper }}Test(TestCase):

    """
        {{ module_name | upper }}Test Model
    """
    def setUp(self):
        """
           create a user
        """
        try:
            self.user = User.objects.get(username='john')
        except User.DoesNotExist:
            self.user = User.objects.create_user(
                username='john', email='john@doe.info', password='doe')

    def create_triggerservice(self, date_created="20130610",
                              description="My first Service", status=True):
        """
           create a TriggerService
        """
        user = self.user

        service_provider = ServicesActivated.objects.create(
            name='ServiceRSS', status=True,
            auth_required=False, description='Service RSS')
        service_consumer = ServicesActivated.objects.create(
            name='Service{{ class_name }}', status=True,
            auth_required=True, description='Service {{ class_name }}')
        provider = UserService.objects.create(user=user,
                                              token="",
                                              name=service_provider)
        consumer = UserService.objects.create(user=user,
                                              token="AZERTY1234",
                                              name=service_consumer)
        return TriggerService.objects.create(provider=provider,
                                             consumer=consumer,
                                             user=user,
                                             date_created=date_created,
                                             description=description,
                                             status=status)

    def create_{{ module_name }}(self):
        """
            Create a {{ class_name }} object related to the trigger object
        """
        trigger = self.create_triggerservice()
        name = '{{ module_name }}'
        status = True
        return {{ class_name | upper }}.objects.create(trigger=trigger, name=name, status=status)

    def test_{{ module_name }}(self):
        """
           Test if the creation of the {{ module_name }} object looks fine
        """
        d = self.create_{{ module_name }}()
        self.assertTrue(isinstance(d, {{ class_name | upper }}))
        self.assertEqual(d.show(), "My {{ class_name }} %s" % d.name)

    """
        Form
    """
    # provider
    def test_valid_provider_form(self):
        """
           test if that form is a valid provider one
        """
        d = self.create_{{ module_name }}()
        data = {'name': d.name}
        form = {{ class_name | upper }}ProviderForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_provider_form(self):
        """
           test if that form is not a valid provider one
        """
        form = {{ class_name | upper }}ProviderForm(data={})
        self.assertFalse(form.is_valid())

    # consumer
    def test_valid_consumer_form(self):
        """
           test if that form is a valid consumer one
        """
        d = self.create_{{ module_name }}()
        data = {'name': d.name}
        form = {{ class_name | upper }}ConsumerForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_consumer_form(self):
        """
           test if that form is not a valid consumer one
        """
        form = {{ class_name | upper }}ConsumerForm(data={})
        self.assertFalse(form.is_valid())

{% if external_api %}
    def test_get_config_th(self):
        """
            does this settings exists ?
        """
        self.assertTrue(settings.TH_{{ module_name | upper }})

{% endif %}