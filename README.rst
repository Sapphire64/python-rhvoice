python-rhvoice
==================

Simple bindings to use excellent `RHVoice <https://github.com/Olga-Yakovleva/RHVoice>`_ library with Python.


Usage
------------------
Add it into a project:

.. code::

	>>> from python-rhvoice import RHVoice


There are two ways to use it, as direct audio output to be manipulated by you:

.. code::

	>>> audio = RHVoice("Преступление и наказание")
	>>> with open('wav.wav', 'wb') as f:
	...     f.write(audio)

	
Or to be saved by this class:

.. code::

	>>> RHVoice("Дневник писателя", output_file="wave.wav")

TODO
------------------
As you can see, code base is simple. It can be improved so feel free to suggest patches with new features.
