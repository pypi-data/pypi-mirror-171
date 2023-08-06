from setuptools import setup, find_packages
from os.path import abspath, dirname, join

def read(rel_path):
   here = abspath(dirname(__file__))
   with open(join(here, rel_path), 'r') as fp:
      return fp.read()

def get_version(rel_path):
   for line in read(rel_path).splitlines():
      if line.startswith('__version__'):
         delim = '"' if '"' in line else "'"
         return line.split(delim)[1]

version = get_version("speeddb/__init__.py")

setup(
   name="speeddb",
   version=version,
   description="SpeedDB",
   author="Nawaf Alqari",
   packages=find_packages(),
   install_requires=[
      'pyonr>=2.0.1',
      'tabulate',
      
   ],
   author_email="nawafalqari13@gmail.com",
   keywords=["speeddb", "db", "speed", "fast", "database"],
   entry_points={
      "console_scripts": ['speeddb=speeddb.cli:runner']
   },
   license="MIT",
   zip_safe=False,
   url='https://github.com/SpeedDB/SpeedDB',
   project_urls={
      'Documentation': 'https://github.com/SpeedDB/SpeedDB#readme',
      'Bug Tracker': 'https://github.com/SpeedDB/SpeedDB/issues',
      'Source Code': 'https://github.com/SpeedDB/SpeedDB',
      'Discord': 'https://discord.gg/cpvynqk4XT',
      'Donate': 'https://paypal.me/NawafHAlqari'
    },
)