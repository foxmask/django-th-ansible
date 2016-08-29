from setuptools import setup, find_packages
from th_{{ module_name }} import __version__ as version
{% if external_api %}
import os


def strip_comments(l):
    return l.split('#', 1)[0].strip()


def reqs(*f):
    return list(filter(None, [strip_comments(l) for l in open(
        os.path.join(os.getcwd(), *f)).readlines()]))

install_requires = reqs('requirements.txt')
{% endif %}

setup(
    name='django_th_{{ module_name }}',
    version=version,
    description='{{ description }}',
    author='{{ author }}',
    author_email='{{ author_email }}',
    url='{{ url }}',
    download_url="{{ download_url }}"
    + version + ".zip",
    packages=find_packages(exclude=['th_{{ module_name }}/local_settings']),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Framework :: Django',
    ],
{% if external_api %}
    install_requires=install_requires,
{% endif %}
    include_package_data=True,
)
