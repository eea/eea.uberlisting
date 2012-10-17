""" Setup.py
"""
from setuptools import setup, find_packages
import os
from os.path import join


NAME = 'eea.uberlisting'
PATH = NAME.split('.') + ['version.txt']
VERSION = open(join(*PATH)).read().strip()

setup(name=NAME,
      version=VERSION,
      description=(
            "Plone product for ajax display of available templates "
            "for the given content type"),
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
          "Framework :: Plone",
          "Framework :: Plone :: 4.0",
          "Framework :: Plone :: 4.1",
          "Framework :: Plone :: 4.2",
          "Programming Language :: Zope",
          "Programming Language :: Python",
          "Topic :: Software Development :: Libraries :: Python Modules",
          "License :: OSI Approved :: GNU General Public License (GPL)",
          "License :: OSI Approved :: Mozilla Public License 1.0 (MPL)",
        ],
      keywords='eea uberlisting templates plone python',
      author='European Environment Agency',
      author_email="webadmin@eea.europa.eu",
      maintainer='David Ichim (Eau de Web)',
      maintainer_email='david.ichim@eaudeweb.ro',
      bugtrack_url="https://github.com/eea/eea.uberlisting/issues",
      download_url="http://pypi.python.org/pypi/eea.uberlisting",
      url='https://github.com/eea/eea.uberlisting/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['eea'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'eea.jquery'
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
