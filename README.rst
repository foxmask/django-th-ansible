=====================
Trigger Happy Ansible
=====================

this project permits to create a new module for Trigger Happy from scratch

Description
===========

This project will create a complet directory tree with all the necessary stuff to be ready to finish to write the main code of your module


Requirements
============

* Ansible 1.9 or 2, as you want, both will work
* MarkupSafe


site.yml
========

the content of the actual looks like this

.. code:: xml

    ---
    # file: site.yml
    # this playbook bootstrap a dummy module
    # with the above informations
    # then your are ready to finish the module ;-)
    - hosts: home-sweet-home

      roles:
      - dummy

      vars:
        # to directory tree and class/module/name purpose
        module_name: johndoe
        class_name: Johndoe

        # for setup.py purpose
        author: John Doe
        author_email: john@doe.com
        description: this is a module that is fun
        details: when fun is higher than anything
        url: https://github.com/foxmask/django-th-johndoe
        download_url: https://github.com/foxmask/django-th-johndoe/archive/trigger-happy-johndoe-

        # for dependencies purpose in the requirements.txt file
        external_api: foobar
        external_api_class: Foobar
        external_api_version: 1.2.3

        # for oauth if any

        oauth_version: ''   # can contain oauth2 or oauth1 or empty

        # URL to access to the OAuth of the service
        AUTH_URL: 'http://foobar.com/oauth/auth'
        ACC_TOKEN: 'http://foobar.com/oauth/access'
        REQ_TOKEN: 'http://foobar.com/oauth/req'


change the value that fit your needs

in case you want to create a module that does not use external_api nor oauth then you could do:

.. code:: xml

    ---
    # file: site.yml
    # this playbook bootstrap a dummy module
    # with the above informations
    # then your are ready to finish the module ;-)
    - hosts: home-sweet-home

      roles:
      - dummy

      vars:
        # to directory tree and class/module/name purpose
        module_name: johndoe
        class_name: Johndoe

        # for setup.py purpose
        author: John Doe
        author_email: john@doe.com
        description: this is a module that is fun
        details: when fun is higher than anything
        url: https://github.com/foxmask/django-th-johndoe
        download_url: https://github.com/foxmask/django-th-johndoe/archive/trigger-happy-johndoe-

        # for dependencies purpose in the requirements.txt file
        external_api: 
        external_api_class:
        external_api_version:

        # for oauth if any

        oauth_version: ''

        # URL to access to the OAuth of the service
        AUTH_URL:
        ACC_TOKEN:
        REQ_TOKEN:


external_api and oauth_version are cleaned up


running
=======

once the file site.yml is ready take a site and launch :

.. code:: bash

    ansible-playbook -i hosts site.yml


and see

.. code:: bash

    PLAY [home-sweet-home] ********************************************************

    GATHERING FACTS ***************************************************************
    ok: [localhost]

    TASK: [dummy | create folder of the module name] ******************************
    changed: [localhost]

    TASK: [dummy | create tests folder of the module name] ************************
    changed: [localhost]

    TASK: [dummy | travis.yml] ****************************************************
    changed: [localhost]

    TASK: [dummy | gitignore] *****************************************************
    changed: [localhost]

    TASK: [dummy | copy of th_dummy/__init__.py] **********************************
    changed: [localhost]

    TASK: [dummy | copy of th_dummy/tests/__init__.py] ****************************
    changed: [localhost]

    TASK: [dummy | copy of LICENSE] ***********************************************
    changed: [localhost]

    TASK: [dummy | copy of MANIFEST.in] *******************************************
    changed: [localhost]

    TASK: [dummy | copy of setup.py] **********************************************
    changed: [localhost]

    TASK: [dummy | copy of README.rst] ********************************************
    changed: [localhost]

    TASK: [dummy | copy of requirements.txt] **************************************
    changed: [localhost]

    TASK: [dummy | copy of my_dummy.py to my_{{ module_name }}.py] ***************
    changed: [localhost]

    TASK: [dummy | copy of model.py] **********************************************
    changed: [localhost]

    TASK: [dummy | copy of forms.py] **********************************************
    changed: [localhost]

    TASK: [dummy | copy of test.py] ***********************************************
    changed: [localhost]

    TASK: [dummy | copy of the templates] *****************************************
    changed: [localhost]

    PLAY RECAP ********************************************************************
    localhost                  : ok=17   changed=16   unreachable=0    failed=0

    (triggerhappy-bootstrap)foxmask@zorro:~/Django-VirtualEnv/django-th-ansible$ ls -ltR django-th-johndoe/
    django-th-johndoe/:
    total 24
    drwxr-xr-x 4 foxmask foxmask 4096 août  23 16:28 th_johndoe
    -rw-r--r-- 1 foxmask foxmask   14 août  23 16:28 requirements.txt
    -rw-r--r-- 1 foxmask foxmask 1368 août  23 16:28 README.rst
    -rw-r--r-- 1 foxmask foxmask 1186 août  23 16:28 setup.py
    -rw-r--r-- 1 foxmask foxmask  194 août  23 16:28 MANIFEST.in
    -rw-r--r-- 1 foxmask foxmask 1484 août  23 16:28 LICENSE

    django-th-johndoe/th_johndoe:
    total 28
    drwxr-xr-x 2 foxmask foxmask 4096 août  23 16:28 tests
    -rw-r--r-- 1 foxmask foxmask  471 août  23 16:28 forms.py
    -rw-r--r-- 1 foxmask foxmask  614 août  23 16:28 models.py
    -rw-r--r-- 1 foxmask foxmask 6424 août  23 16:28 my_johndoe.py
    -rw-r--r-- 1 foxmask foxmask   81 août  23 16:28 __init__.py
    drwxr-xr-x 3 foxmask foxmask 4096 août  23 16:28 templates

    django-th-johndoe/th_johndoe/tests:
    total 4
    -rw-r--r-- 1 foxmask foxmask 3725 août  23 16:28 test.py
    -rw-r--r-- 1 foxmask foxmask    0 août  23 16:28 __init__.py

    django-th-johndoe/th_johndoe/templates:
    total 4
    drwxr-xr-x 2 foxmask foxmask 4096 août  23 16:28 th_johndoe

    django-th-johndoe/th_johndoe/templates/th_johndoe:
    total 20
    -rw-r--r-- 1 foxmask foxmask 1277 août  23 16:28 edit_provider.html
    -rw-r--r-- 1 foxmask foxmask 1277 août  23 16:28 edit_consumer.html
    -rw-r--r-- 1 foxmask foxmask 1513 août  23 16:28 wz-3-form.html
    -rw-r--r-- 1 foxmask foxmask 1513 août  23 16:28 wz-1-form.html
    -rw-r--r-- 1 foxmask foxmask  382 août  23 16:28 callback.html


last step
=========

change the string "Dummy" in all the templates


.. code:: bash
   
   sed -i -e 's/Dummy/JohnDoe/' django-th-johndoe/th_johndoe/templates/th_johndoe/callback.html
   sed -i -e 's/Dummy/JohnDoe/' django-th-johndoe/th_johndoe/templates/th_johndoe/wz-1-form.html
   sed -i -e 's/Dummy/JohnDoe/' django-th-johndoe/th_johndoe/templates/th_johndoe/wz-3-form.html

Finally
=======

Once it is done "django-th-johndoe" is ready to be pushed on a repository of your own.

But if you plan to make a pull request to TriggerHappy project, you will just need to keep the directory "th_johndoe" 


.. _TriggerHappy: https://github.com/foxmask/django-th/
