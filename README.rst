crc8
====

.. image:: https://travis-ci.org/niccokunzmann/crc8.svg
   :target: https://travis-ci.org/niccokunzmann/crc8
   :alt: Build Status

.. image:: https://badge.fury.io/py/crc8.svg
   :target: https://pypi.python.org/pypi/crc8
   :alt: Python Package Version on Pypi
   
.. image:: https://img.shields.io/pypi/dm/crc8.svg
   :target: https://pypi.python.org/pypi/crc8#downloads
   :alt: Downloads from Pypi   

   
A module that implements the CRC8 hash algorithm for Python 2 and 3.

Installation
------------

.. code:: bash

    pip install crc8

Or copy the `crc8.py
<https://github.com/niccokunzmann/crc8/blob/master/crc8.py>`__ file somewhere
where you can import it.

Usage
-----

The ``crc8`` class has the same interface as the hash functions in the 
`hashlib module
<https://docs.python.org/2/library/hashlib.html>`__.

Example:

.. code:: python

    import crc8
    hash = crc8.crc8()
    hash.update(b'123')
    assert hash.hexdigest() == 'c0'

Contribute
----------

If something s not there that you would like to have, 
`open an issue <https://github.com/niccokunzmann/crc8/issues>`__, 
`create a pull request <https://github.com/niccokunzmann/crc8/pulls>`__.

The license is `MIT
<https://github.com/niccokunzmann/crc8/blob/master/LICENSE>`__ and
I value contributions if you modify the code.