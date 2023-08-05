Splittic AI
===========

Reference: https://ai.dragonspot.tk
-----------------------------------

Pricing
-------

10 € / 100k API uses

How to
------

Install
~~~~~~~

.. code:: python

   pip install splitticai
   from splitticai import AI
   bot = AI('API KEY')

Image Generation
~~~~~~~~~~~~~~~~

.. code:: python

   bot.makeimg('Text Input', 'imagefile.png')

File will be saved to imagefile.png ### Question/Answer

.. code:: python

   answer = bot.qa('Question?')

Conversation
~~~~~~~~~~~~

.. code:: python

   answer = bot.qa('Message', int(userid))

URL Malware Scan
~~~~~~~~~~~~~~~~

.. code:: python

   issafe = bot.scan('URL')

Returns the security risk. Risks are ``Minimal Security Risk``,
``Low Security Risk``, ``Medium Security Risk``, ``High Security Risk``
and ``Very High Security Risk``.
