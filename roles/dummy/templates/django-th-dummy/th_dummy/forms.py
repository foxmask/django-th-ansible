# coding: utf-8

from django import forms
from django.forms import TextInput
from th_{{ module_name }}.models import {{ class_name }}


class {{ class_name }}Form(forms.ModelForm):

    """
        for to handle Pocket service
    """

    class Meta:
        model = {{ class_name }}
        fields = ('name',)
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
        }


class {{ class_name }}ProviderForm({{ class_name }}Form):
    pass


class {{ class_name }}ConsumerForm({{ class_name }}Form):
    pass
