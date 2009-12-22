#!/usr/bin/env python

from distutils.core import setup

def do_setup():
    dist = setup(
        name='Docutils phpDoc (DocBook) XML Writer',
        description='A phpDoc (DocBook) XML Writer for Docutils',
        url='http://xdissent.com',
        version='0.1',
        author='Greg Thornton',
        author_email='xdissent@gmail.com',
        license='GPL',
        packages=['docutils.writers'],
        package_dir={'docutils.writers':'writer'},
        scripts=['rst2phpdoc.py']
    )
    return dist

if __name__ == '__main__':
    do_setup()