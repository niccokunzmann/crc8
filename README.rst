crc8
====

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
    assert hash.digest() == b'\xc0'
    hash.reset()
    assert hash.hexdigest() == '00'

You can also use the method chaining syntax:

.. code:: python

    import crc8
    hash = crc8.crc8()
    result = hash.reset().update(b'123').hexdigest()
    assert result == 'c0'

Contribute
----------

If something s not there that you would like to have, 
`open an issue <https://github.com/niccokunzmann/crc8/issues>`__, 
`create a pull request <https://github.com/niccokunzmann/crc8/pulls>`__.

The license is `MIT
<https://github.com/niccokunzmann/crc8/blob/master/LICENSE>`__ and
I value contributions if you modify the code.


Changelog
---------

- v0.2.1 - add method chaining
- v0.2.0 - add ``reset()`` by `henriksod <https://github.com/henriksod>`_
- v0.1.0 - add option to select initial polynom by `FevGeb <https://github.com/FevGeb>`_
- v0.0.5 - document license
- v0.0.4 - choose MIT license

Release
-------

Install `twine <https://twine.readthedocs.io/en/stable/>`_.

.. code:: sh

    python setup.py sdist
    source .env # if you have stored TWINE_USERNAME and TWINE_PASSWORD
    twine upload dist/*
    
    
