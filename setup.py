"""

(c) 2019 by Simple Analytics. All rights reserved.

This program is distributed in the hope that it will be useful, but is provided AS IS with ABSOLUTELY NO WARRANTY;
The entire risk as to the quality and performance of the program is with you. Should the program prove defective,
you assume the cost of all necessary servicing, repair or correction. In no event will any of the developers, or
any other party, be liable to anyone for damages arising out of the use or inability to use the program.
You may copy and distribute copies of the Program, provided that you keep intact all the notices that refer to the
absence of any warranty.

"""
from setuptools import setup


setup(
    name='simpleanalytics',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Environment :: Plugins",
        "License :: OSI Approved :: MIT License",
        # supported python versions
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Page Counters",
        "Framework :: Django :: 1.8",
        "Framework :: Django :: 1.9",
        "Framework :: Django :: 2.0",
        "Framework :: Django :: 2.1",
        "Framework :: Django :: 2.2",
    ],
    version='0.1.4',
    description='simpleanalytics templatetags for Django',
    packages=['simpleanalytics', 'simpleanalytics.templatetags', ],
    author='simpleanalytics.io',
    author_email='support@mail.simpleanalytics.io',
)