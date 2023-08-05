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
.. |docs| image:: https://readthedocs.org/projects/hummingbird-joystick/badge/?style=flat
    :target: https://hummingbird-joystick.readthedocs.io/
    :alt: Documentation Status

.. |github-actions| image:: https://github.com/fmorton/hummingbird-joystick/actions/workflows/github-actions.yml/badge.svg
    :alt: GitHub Actions Build Status
    :target: https://github.com/fmorton/hummingbird-joystick/actions

.. |requires| image:: https://requires.io/github/fmorton/hummingbird-joystick/requirements.svg?branch=main
    :alt: Requirements Status
    :target: https://requires.io/github/fmorton/hummingbird-joystick/requirements/?branch=main

.. |codecov| image:: https://codecov.io/gh/fmorton/hummingbird-joystick/branch/main/graphs/badge.svg?branch=main
    :alt: Coverage Status
    :target: https://codecov.io/github/fmorton/hummingbird-joystick

.. |version| image:: https://img.shields.io/pypi/v/hummingbird-joystick.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/hummingbird-joystick

.. |wheel| image:: https://img.shields.io/pypi/wheel/hummingbird-joystick.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/hummingbird-joystick

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/hummingbird-joystick.svg
    :alt: Supported versions
    :target: https://pypi.org/project/hummingbird-joystick

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/hummingbird-joystick.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/hummingbird-joystick

.. |commits-since| image:: https://img.shields.io/github/commits-since/fmorton/hummingbird-joystick/v0.0.1.svg
    :alt: Commits since latest release
    :target: https://github.com/fmorton/hummingbird-joystick/compare/v0.0.1...main



.. end-badges

Support for Birdbrain Technolgies Hummingbird joystick

* Free software: MIT license

Installation
============

::

    pip install hummingbird-joystick

You can also install the in-development version with::

    pip install https://github.com/fmorton/hummingbird-joystick/archive/main.zip


Documentation
=============


https://hummingbird-joystick.readthedocs.io/


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
