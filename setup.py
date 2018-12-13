import sys

try:
    from setuptools import setup

except ImportError:
    from distutils.core import setup

if sys.version_info <= (2, 4):
    error = 'Requires Python Version 2.5 or above... Exiting.'

requirements = [
    'requests>=2.11.1,<3.0',
]

setup(name='smartmonkey',
      version='0.0.2',
      description='Python client for Smartmonkey API Web Services',
      scripts=[],
      url='', #TODO: Include repo url
      packages=['smartmonkey'],
      license='Apache 2.0',
      platforms='Posix; MacOS X; Windows',
      setup_requires=requirements,
      install_requires=requirements,
      classifiers=['Development Status :: 4 - Beta',
                   'Intended Audience :: Developers',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3.2',
                   'Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: 3.5',
                   'Programming Language :: Python :: 3.6',
                   ]
    )
