{% if False %}
# Django 1.4 Base Template #

## About ##

Fork of https://github.com/xenith/django-base-template with some things added/removed to fit my style.
## How to use this template to create your project ##

- Create your virtualenv
- Install Django 1.4
- $ django-admin.py startproject --template https://github.com/ryanrdetzel/django-base-template/zipball/master --extension py,md projectname
- $ cd projectname
- $ pip install -r requirements/dev.txt
- $ cp projectname/settings/local-dist.py projectname/settings/local.py (local.py shouldn't be added
  to your source control)
  $ setup mysql settings in local.py
- $ ./manage.py syncdb
- $ ./manage.py runserver

{% endif %}
# {{ project_name|title }} Project #

## About ##

## Prerequisites ##

- Python >= 2.5
- pip
- virtualenv (virtualenvwrapper is recommended for use during development)

License
-------
This software is licensed under the [New BSD License][BSD]. For more
information, read the file ``LICENSE``.

[BSD]: http://opensource.org/licenses/BSD-3-Clause
