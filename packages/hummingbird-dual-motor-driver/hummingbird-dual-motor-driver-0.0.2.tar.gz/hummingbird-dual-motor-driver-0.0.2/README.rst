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
.. |docs| image:: https://readthedocs.org/projects/hummingbird-dual-motor-driver/badge/?style=flat
    :target: https://hummingbird-dual-motor-driver.readthedocs.io/
    :alt: Documentation Status

.. |github-actions| image:: https://github.com/fmorton/hummingbird-dual-motor-driver/actions/workflows/github-actions.yml/badge.svg
    :alt: GitHub Actions Build Status
    :target: https://github.com/fmorton/hummingbird-dual-motor-driver/actions

.. |requires| image:: https://requires.io/github/fmorton/hummingbird-dual-motor-driver/requirements.svg?branch=main
    :alt: Requirements Status
    :target: https://requires.io/github/fmorton/hummingbird-dual-motor-driver/requirements/?branch=main

.. |codecov| image:: https://codecov.io/gh/fmorton/hummingbird-dual-motor-driver/branch/main/graphs/badge.svg?branch=main
    :alt: Coverage Status
    :target: https://codecov.io/github/fmorton/hummingbird-dual-motor-driver

.. |version| image:: https://img.shields.io/pypi/v/hummingbird-dual-motor-driver.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/hummingbird-dual-motor-driver

.. |wheel| image:: https://img.shields.io/pypi/wheel/hummingbird-dual-motor-driver.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/hummingbird-dual-motor-driver

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/hummingbird-dual-motor-driver.svg
    :alt: Supported versions
    :target: https://pypi.org/project/hummingbird-dual-motor-driver

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/hummingbird-dual-motor-driver.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/hummingbird-dual-motor-driver

.. |commits-since| image:: https://img.shields.io/github/commits-since/fmorton/hummingbird-dual-motor-driver/v0.0.1.svg
    :alt: Commits since latest release
    :target: https://github.com/fmorton/hummingbird-dual-motor-driver/compare/v0.0.1...main



.. end-badges

A dual motor driver for Birdbrain Technologies Hummingbird

* Free software: MIT license

Installation
============

::

    pip install hummingbird-dual-motor-driver

You can also install the in-development version with::

    pip install https://github.com/fmorton/hummingbird-dual-motor-driver/archive/main.zip


Documentation
=============


https://hummingbird-dual-motor-driver.readthedocs.io/


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
