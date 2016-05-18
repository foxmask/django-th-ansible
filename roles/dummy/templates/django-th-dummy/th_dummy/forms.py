# coding: utf-8

from django import forms
from django.forms import TextInput
from th_{{ module_name }}.models import {{ class_name | upper}}


class {{ class_name }}Form(forms.ModelForm):

    """
        for to handle {{ class_name }} service
    """

    class Meta:
        model = {{ class_name | upper }}
        fields = ('name',)
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
        }


class {{ class_name | upper }}ProviderForm({{ class_name | upper }}Form):
    pass


class {{ class_name | upper }}ConsumerForm({{ class_name | upper }}Form):
    pass
