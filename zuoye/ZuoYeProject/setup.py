import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'pyramid',
    'SQLAlchemy',
    'transaction',
    'pyramid_tm',
    'pyramid_debugtoolbar',
    'zope.sqlalchemy',
    'waitress',
    # jiawzhang: add a new docutils package for MyProject app.
    # After adding this new dependency, enter virtual env, re-run 'python setup.py develop' in MyProject path to download and install the dependency.
    'WebTest', # jiawzhang: add for running unit test.
    ]

setup(name='ZuoYeProject',
      version='0.0',
      description='ZuoYeProject',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='zuoyeproject',
      install_requires=requires,
      # jiawzhang: ./myproject/scripts/initializedb.py sepcified below is executed when running "python setup.py develop"
      entry_points="""\
      [paste.app_factory]
      main = zuoyeproject:main
      [console_scripts]
      initialize_ZuoYeProject_db = zuoyeproject.scripts.initializedb:main
      """,
      )

