# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from recaptcha import __version__

long_desc = open('README.rst', 'rb').read().decode('utf-8') + '\n\n' + \
            open('AUTHORS.rst', 'rb').read().decode('utf-8') + '\n\n' + \
            open('CHANGELOG.rst', 'rb').read().decode('utf-8')
setup(
    name='js-recaptcha',
    version=__version__,
    description=open('README.rst').read(),
    author='Compound Partners Ltd',
    author_email='hello@compoundpartners.co.uk',
    long_description=long_desc,
    license='GPLv3',
    url='https://github.com/compoundpartners/js-recaptcha',
    packages=find_packages(),
    platforms=['OS Independent'],
    install_requires=[
        'django',
    ],
    tests_require=[
        'django-setuptest>=0.2.1',
    ],
    test_suite="setuptest.setuptest.SetupTestSuite",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 1.11',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
    include_package_data=True,
    zip_safe=False,
)
