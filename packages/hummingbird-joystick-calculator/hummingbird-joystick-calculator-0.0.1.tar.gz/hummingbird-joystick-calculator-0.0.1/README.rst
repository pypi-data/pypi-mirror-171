========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |github-actions| |requires|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/python-hummingbird-joystick-calculator/badge/?style=flat
    :target: https://python-hummingbird-joystick-calculator.readthedocs.io/
    :alt: Documentation Status

.. |github-actions| image:: https://github.com/fmorton/python-hummingbird-joystick-calculator/actions/workflows/github-actions.yml/badge.svg
    :alt: GitHub Actions Build Status
    :target: https://github.com/fmorton/python-hummingbird-joystick-calculator/actions

.. |requires| image:: https://requires.io/github/fmorton/python-hummingbird-joystick-calculator/requirements.svg?branch=main
    :alt: Requirements Status
    :target: https://requires.io/github/fmorton/python-hummingbird-joystick-calculator/requirements/?branch=main

.. |codecov| image:: https://codecov.io/gh/fmorton/python-hummingbird-joystick-calculator/branch/main/graphs/badge.svg?branch=main
    :alt: Coverage Status
    :target: https://codecov.io/github/fmorton/python-hummingbird-joystick-calculator

.. |version| image:: https://img.shields.io/pypi/v/hummingbird-joystick-calculator.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/hummingbird-joystick-calculator

.. |wheel| image:: https://img.shields.io/pypi/wheel/hummingbird-joystick-calculator.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/hummingbird-joystick-calculator

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/hummingbird-joystick-calculator.svg
    :alt: Supported versions
    :target: https://pypi.org/project/hummingbird-joystick-calculator

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/hummingbird-joystick-calculator.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/hummingbird-joystick-calculator

.. |commits-since| image:: https://img.shields.io/github/commits-since/fmorton/python-hummingbird-joystick-calculator/v0.0.1.svg
    :alt: Commits since latest release
    :target: https://github.com/fmorton/python-hummingbird-joystick-calculator/compare/v0.0.1...main



.. end-badges

Calculator for the hummingbird_joystick package converting xy coordinates from the joystick to left/right motor speeds.

* Free software: MIT license

Installation
============

::

    pip install hummingbird-joystick-calculator

You can also install the in-development version with::

    pip install https://github.com/fmorton/python-hummingbird-joystick-calculator/archive/main.zip


Documentation
=============


https://python-hummingbird-joystick-calculator.readthedocs.io/


Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
