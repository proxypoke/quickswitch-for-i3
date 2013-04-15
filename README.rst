quickswitch for i3
==================

Overview
--------
This utility for i3, inspired by Pentadactyl's ``:buffers`` command, allows
you to quickly switch to and locate windows on all your workspaces, using an
interactive dmenu prompt.

It also provides a similiar facility for scratchpad windows, which can be used
by passing the ``-s`` or ``--scratchpad`` flag. If you don't want to jump to the
window's workspace, but instead move the window to your curren workspace, use
``-m`` or ``--move``. There's also a flag for jumping to workspaces by name -
``-w`` or ``--workspaces`` - which might be useful if you have many named
workspaces.

Here's how it looks in action:

.. image:: http://i.imgur.com/QeQrM.png


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

License
-------
**Disclaimer: quickswitch-i3 is a third party script and in no way affiliated
with the i3 project.**

This program is free software under the terms of the
Do What The Fuck You Want To Public License.
It comes without any warranty, to the extent permitted by
applicable law. For a copy of the license, see COPYING or
head to http://sam.zoy.org/wtfpl/COPYING.
