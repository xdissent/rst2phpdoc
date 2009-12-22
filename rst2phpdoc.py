#!/usr/bin/env python

import locale
try:
    locale.setlocale(locale.LC_ALL, '')
except:
    pass

from docutils.core import publish_cmdline, default_description

description = ('Generates phpDoc (DocBook) XML documents from standalone '
               'reStructuredText sources.  ' + default_description)

publish_cmdline(writer_name='phpdoc', description=description)