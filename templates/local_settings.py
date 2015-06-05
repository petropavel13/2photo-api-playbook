# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '{{ db.name }}',
        'HOST': '{{ db.host }}',
        'USER': '{{ db.user }}',
        'PASSWORD': '{{ db.password }}',
    }
}