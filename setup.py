# quickswitch for i3 - quickly change to and locate windows in i3.
#
# Author: slowpoke <mail+python at slowpoke dot io>
#
# This program is Free Software under the terms of the
#
#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#                    Version 2, December 2004
#
# Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>
#
# Everyone is permitted to copy and distribute verbatim or modified
# copies of this license document, and changing it is allowed as long
# as the name is changed.
#
#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
#
#  0. You just DO WHAT THE FUCK YOU WANT TO.

from distutils.core import setup

import quickswitch

setup(name='quickswitch-i3',
      description='Quickly change to and locate windows in i3',
      long_description=open('README.rst').read(),
      version=quickswitch.__version__,
      author='slowpoke',
      author_email='mail+python at slowpoke dot io',
      url='https://github.com/proxypoke/quickswitch-for-i3',
      scripts=['quickswitch.py'],
      requires=['i3_py'],
      classifiers=['Intended Audience :: End Users/Desktop',
                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 3'],
      license='DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE')
