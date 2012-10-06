#!/usr/bin/env python
# quickswitch for i3 - quickly change to and locate windows in i3.
#
# Author: slowpoke <mail+python at slowpoke dot io>
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

__version__ = '1.0'


import subprocess
import i3


def dmenu(options):
    '''Call dmenu with a list of options.'''
    cmd = subprocess.Popen(['dmenu', '-b', '-i', '-l', '20'],
                           stdin=subprocess.PIPE,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)
    stdout, _ = cmd.communicate('\n'.join(options).encode('utf-8'))
    return stdout.decode('utf-8').strip('\n')


def main():
    windows = i3.filter(nodes=[])
    lookup = {}
    for window in windows:
        name = window.get('name')
        id_ = window.get('window')
        if id_ is None:
            # this is not an X window, ignore it
            continue
        lookup[name] = id_

    target = dmenu(lookup.keys())
    id_ = lookup.get(target)
    success = i3.focus(id=lookup.get(target)) if id_ is not None else False

    exit(0 if success else 1)


if __name__ == '__main__':
    main()
