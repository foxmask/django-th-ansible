===============
{{ module_name }}
===============

{{ description }}

{{ details }}

Requirements :
==============

* django_th == 0.11.0


Installation:
=============

to get the project, from your virtualenv, do :

.. code:: python

    pip install django-th-{{ module_name }}

then do

.. code:: python

    python manage.py migrate

to update the database

Parameters :
============

As usual you will setup the database parameters.

Important parts are the settings of the available services :

Settings.py
-----------

INSTALLED_APPS
~~~~~~~~~~~~~~

add the module th_{{ module_name }} to INSTALLED_APPS

.. code:: python

    INSTALLED_APPS = (
        'th_{{ module_name }}',
    )


TH_SERVICES
~~~~~~~~~~~

TH_SERVICES is a list of the services used by Trigger Happy

.. code:: python

    TH_SERVICES = (
        'th_{{ module_name }}.my_{{ module_name }}.Service{{ module_name | capitalize }}',
    )

{% if oauth_version %}
TH_{{module_name }}
~~~~~~~~

TH_{{ module_name }} is the settings you will need to be able to add/read data in/from {{ module_name }} Service.

.. code:: python

    TH_{{ module_name | upper }} = {
        'consumer_key': 'abcdefghijklmnopqrstuvwxyz',
    }

{% endif %}
Setting up : Administration
===========================

once the module is installed, go to the admin panel and activate the service dummy.

All you can decide here is to tell if the service requires an external authentication or not.

Once they are activated. User can use them.
