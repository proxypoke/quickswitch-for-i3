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

__version__ = '1.1'


import argparse
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


def get_windows():
    windows = i3.filter(nodes=[])
    return filter_windows(windows)


def get_scratchpad():
    scratchpad = i3.filter(name="__i3_scratch")[0]
    nodes = scratchpad["floating_nodes"]
    windows = i3.filter(tree=nodes, nodes=[])
    return filter_windows(windows)


def filter_windows(windows):
    lookup = {}
    for window in windows:
        name = window.get('name')
        id_ = window.get('window')
        if id_ is None:
            # this is not an X window, ignore it.
            continue
        if name.startswith("i3bar for output"):
            # this is an i3bar, ignore it.
            continue
        lookup[name] = id_
    print(lookup)
    return lookup


def get_scratchpad_window(window):
    '''Does `scratchpad show` on the specified window.'''
    return i3.scratchpad("show", id=window)


def focus(window):
    '''Focuses the given window.'''
    return i3.focus(id=window)


def main():
    parser = argparse.ArgumentParser(description='''quickswitch for i3''')
    parser.add_argument('-s', '--scratchpad', default=False, action="store_true",
                        help="list scratchpad windows instead of regular ones")
    args = parser.parse_args()

    lookup_func = get_scratchpad if args.scratchpad else get_windows
    focus_func = get_scratchpad_window if args.scratchpad else focus

    lookup = lookup_func()
    target = dmenu(lookup.keys())
    id_ = lookup.get(target)
    success = focus_func(lookup.get(target)) if id_ is not None else False

    exit(0 if success else 1)


if __name__ == '__main__':
    main()
