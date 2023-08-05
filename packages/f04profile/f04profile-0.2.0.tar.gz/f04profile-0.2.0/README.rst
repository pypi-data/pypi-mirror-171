================
MYSTRAN profiler
================

MYSTRAN F04 log file parser

Features
========

This package installs a ``f04prof`` command.

Usage
=====

Create a .prof file by entering the following command::

        $ f04prof path/to/myfile.F04

This will create ``path/to/myfile.prof``. You can then visualize it with ``snakeviz`` (`<https://https://pypi.org/project/snakeviz/>`_).

To automatically trigger snakeviz, pass ``-s`` flag::


        $ f04prof -s path/to/myfile.F04

Or::

        $ f04prof path/to/myfile.F04 -s

Install
=======

The installation process will install ``snakeviz`` as dependency. Use ``pipx`` to install it in a user contained environment::

        $ pipx install f04profile
