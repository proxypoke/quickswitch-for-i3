quickswitch for i3
==================

Overview
--------
This utility for i3_, inspired by Pentadactyl_'s ``:buffers`` command, allows
you to quickly switch to and locate windows on all your workspaces, using an
interactive dmenu prompt. It has since gained a lot of other functionality to
make working with i3 even more efficient.

Usage
-----
Finding windows
~~~~~~~~~~~~~~~

The core functionality of quickswitch is still finding windows and jumping to
them, and this is what it does when you call it without any options.

Here's how it looks in action:

.. image:: http://i.imgur.com/QeQrM.png

However, sometimes you may want to grab a window and move it to your current
workspace. This can be done with the ``-m/--move`` flag.

A similiar feature is the ``-s/--scratchpad`` flag, which searches your
scratchpad, and does a ``scratchpad show`` on the window you choose.

You can also search and jump (or move) via regular expression using the
``-r``/``--regex`` flag, without using dmenu. This could be useful for
scripting, or if you are a regex wizard who feels limited by dmenu.

Workspaces
~~~~~~~~~~

quickswitch also provides a few functions to manage workspaces. First of
all, it allows you to search workspaces in the same fashion as windows with the
``-w/--workspaces`` flag. This is *extremely* useful for working with many named
workspaces without having them bound to any particular key.

Another useful feature is to quickly get an empty workspace. This is what the
``-e/--empty`` flag does: it will jump you to the first empty, numbered
workspace.

If you use this excessively, then your numbered workspaces might fragment a lot.
You can fix this easily with ``-g``/``--degap``, which "defragments" your
workspaces, without affecting their order (eg, [1, 4, 7] becomes [1, 2, 3] by
renaming 4 to 2 and 7 to 3).

dmenu
~~~~~

You can influence how dmenu is called with the ``-d/--dmenu`` flag, which
expects a complete dmenu command. The default is ``dmenu -b -i -l 20`` (which
makes dmenu appear on the bottom of your screen (-b) in a vertical manner with
at most 20 lines (-l 20), and matches case insensitively (-i). See the man page
for dmenu for a list of options.

**Note:** The versions of quickswitch before 2.0 used explicit flags for changing
dmenu's behavior. This was rather inflexible, because it needed an explicit flag
for every dmenu option, and it hardcoded the dmenu command. For most people, the
default should be fine, but if you want to change anything, this allows you to
go wild.

Dependencies
------------
quickswitch-i3 requires dmenu (which you likely already have installed), and
i3-py, which you can install with ``pip install i3-py``.

quickswitch-i3 was tested in Python 2.7.3 and 3.2.3. It will not work in version
prior to 2.7 due to the usage of ``argparse``.

Installation
------------
quickswitch-i3 has a PyPI entry, so you can install it with ``pip install
quickswitch-i3``. Alternatively, you can always manually run the setup file with
``python setup.py install``.

Additionally, if you are an Arch user, you can install it from the AUR. The
package is called ``quickswitch-i3``. The PKGBUILD is also included here.

**NOTE**: I do not maintain the AUR package anymore, since I do not have access
to any Arch box. See comment on the AUR page.

An overlay for Gentoo is in the works.

Contributions
-------------
...are obviously welcome. Pretty much every feature in quickswitch originated
because someone (not just me) thought "hey, this would be useful". Just shoot a
Pull Request.

License
-------
**Disclaimer: quickswitch-i3 is a third party script and in no way affiliated
with the i3 project.**

This program is free software under the terms of the
Do What The Fuck You Want To Public License.
It comes without any warranty, to the extent permitted by
applicable law. For a copy of the license, see COPYING or
head to http://sam.zoy.org/wtfpl/COPYING.

.. _Pentadactyl: http://5digits.org/pentadactyl/
.. _i3: http://i3wm.org
