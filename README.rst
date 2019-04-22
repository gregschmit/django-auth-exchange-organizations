Auth Exchange Organizations
###########################

Source: https://github.com/gregschmit/django-auth-exchange-organizations

PyPI: https://pypi.org/project/django-auth-exchange-organizations/

Auth Exchange Organizations is an extension to Auth Exchange
(https://github.com/gregschmit/django-auth-exchange) that allows
users/domains to be associated to Organizations from
:code:`django-organizations`.


How to Use
==========

.. code-block:: shell

    $ pip install django-auth-exchange-organizations

Include :code:`django_auth_exchange_organizations` in your
:code:`INSTALLED_APPS`.

You can create associations by creating DomainOrganization objects in the Admin
UI. You'll need to configure :code:`django-auth-exchange` before you can test
this app out.


Settings
--------

:code:`AUTH_EXCHANGE_ORGS_AUTOASSOCIATE` (default: :code:`True`) - Whether
organization association should be automatic.

:code:`AUTH_EXCHANGE_ORGS_AUTO_CREATE_ORGS` (default: :code:`True`) - Whether
organizations/associations should be created if they don't exist.


Contributing
============

Email gschmi4@uic.edu if you want to contribute. You must only contribute code
that you have authored or otherwise hold the copyright to, and you must
make any contributions to this project available under the MIT license.

To collaborators: don't push using the :code:`--force` option.
