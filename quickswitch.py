#!/usr/bin/env python
# -*- coding: utf-8 -*-
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

__version__ = '1.3'


import argparse
import subprocess
import os

try:
    import i3
except ImportError:
    print("quickswitch requires i3-py.")
    print("You can install it from the PyPI with ``pip install i3-py''.")
    exit(1)


def check_dmenu():
    '''Check if dmenu is available.'''
    try:
        devnull = open(os.devnull)
        subprocess.Popen(
            ['dmenu', '-h'], stdout=devnull, stderr=devnull).communicate()
    except OSError as e:
        if e.errno == os.errno.ENOENT:
            return False
    return True


def dmenu(options):
    '''Call dmenu with a list of options.'''
    cmd = subprocess.Popen(['dmenu', '-b', '-i', '-l', '20'],
                           stdin=subprocess.PIPE,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)
    stdout, _ = cmd.communicate('\n'.join(options).encode('utf-8'))
    return stdout.decode('utf-8').strip('\n')


def get_windows():
    '''Get all windows.'''
    windows = i3.filter(nodes=[])
    return filter_windows(windows)


def get_scratchpad():
    '''Get all windows on the scratchpad.'''
    scratchpad = i3.filter(name="__i3_scratch")[0]
    nodes = scratchpad["floating_nodes"]
    windows = i3.filter(tree=nodes, nodes=[])
    return filter_windows(windows)


def get_workspaces():
    '''Returns all workspace names.

    NOTE: This returns a map of name → name, which is rather redundant, but
    makes it possible to use the result without changing much in main().
    '''
    workspaces = i3.get_workspaces()
    for ws in workspaces:
        # filter_windows will set the value of all entries in the lookup table
        # to the window id. We act as if the workspace name is the window id.
        ws['window'] = ws['name']
    return filter_windows(workspaces)


def filter_windows(windows):
    '''Create a lookup table from the given list of windows.

    The returned dict is in the format window title → X window id.
    '''
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
    return lookup


def get_scratchpad_window(window):
    '''Does `scratchpad show` on the specified window.'''
    return i3.scratchpad("show", id=window)


def move_window_here(window):
    '''Does `move workspace current` on the specified window.'''
    return i3.msg(0, "%s move workspace current" % i3.container(id=window))


def focus(window):
    '''Focuses the given window.'''
    return i3.focus(id=window)


def goto_workspace(name):
    '''Jump to the given workspace.'''
    return i3.workspace(name)


def main():
    parser = argparse.ArgumentParser(description='''quickswitch for i3''')
    parser.add_argument('-m', '--move', default=False, action="store_true",
                        help="move window to the current workspace")

    mutgrp = parser.add_mutually_exclusive_group()
    mutgrp.add_argument('-s', '--scratchpad', default=False, action="store_true",
                        help="list scratchpad windows instead of regular ones")
    mutgrp.add_argument('-w', '--workspaces', default=False,
                        action="store_true",
                        help="list workspaces instead of windows")
    args = parser.parse_args()

    if not check_dmenu():
        print("quickswitch requires dmenu.")
        print("Please install it using your distribution's package manager.")
        exit(1)

    lookup_func = get_windows
    if args.scratchpad:
        lookup_func = get_scratchpad
    if args.workspaces:
        lookup_func = get_workspaces

    action_func = focus
    if args.move:
        action_func = move_window_here
    else:
        if args.scratchpad:
            action_func = get_scratchpad_window
        if args.workspaces:
            action_func = goto_workspace

    lookup = lookup_func()
    target = dmenu(lookup.keys())
    id_ = lookup.get(target)
    success = action_func(lookup.get(target)) if id_ is not None else False

    exit(0 if success else 1)


if __name__ == '__main__':
    main()
