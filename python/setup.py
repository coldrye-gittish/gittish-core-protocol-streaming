#!/usr/bin/env python3

import os
from setuptools import setup


def resolve_meta():
  result = {}
  f = open('META')
  contents = f.read()
  f.close()
  for line in contents.split('\n'):
    if ' = ' in line:
      attr, value = line.split(' = ')
      result[attr] = value.replace('\'', '')
  return result


def _resolve_packages(root, rel_path, nsonly = False):
  result = []
  it = os.scandir(root)
  isnspackage = True
  for entry in it:
    if entry.is_dir():
      nrel_path = []
      nrel_path.extend(rel_path)
      nrel_path.append(entry.name)
      result.extend(_resolve_packages(entry.path, nrel_path, nsonly = nsonly))
    elif entry.is_file() and entry.name == '__init__.py':
      if not nsonly:
        result.append('.'.join(rel_path))
      isnspackage = False
      break
  if isnspackage and nsonly:
    result.append('.'.join(rel_path))
  return result


def resolve_namespace_packages(*roots):
  result = []
  for root in roots:
    rel_path = [root]
    result.extend(_resolve_packages('./' + root, rel_path, nsonly = True))
  return sorted(result)


def resolve_packages(*roots):
  result = []
  for root in roots:
    rel_path = [root]
    result.extend(_resolve_packages('./' + root, rel_path))
  return sorted(result)


def resolve_requirements():
  result = []
  try:
    f = open('requirements.txt', 'r')
    contents = f.read()
    f.close()
    for line in contents.split('\n'):
      result.append(line.strip())
  except:
    pass
  return result


meta = resolve_meta()

setup(
  name=meta['PACKAGE'],
  version=meta['VERSION'],

  license=meta['LICENSE'],

  description=meta['DESCRIPTION'],
  long_description='',
  url=meta['URL'],

  classifiers=[
    meta['DEV_STATUS'],
    meta['LICENSE'],
    meta['OS'],
    'Intended Audience :: Developers',
    'Programming Language :: Python :: 3',
    'Topic :: Software Development :: Version Control',
    'Topic :: Software Development :: Libraries :: Python Modules'
  ],

  author=meta['AUTHOR'],
  author_email=meta['AUTHOR_EMAIL'],

  namespace_packages=resolve_namespace_packages('gittish'),
  packages=resolve_packages('gittish'),

  install_requires=resolve_requirements(),

  zip_safe=bool(meta['ZIP_SAFE'])
)

# vim: expandtab:ts=2:sw=2:
