python-rhvoice
==================

Simple bindings to use excellent `RHVoice <https://github.com/Olga-Yakovleva/RHVoice>`_ library with Python.


Usage
------------------
Download or clone this project, then install it:

.. code::

	$ python3 setup.py install

Add it into your project:

.. code::

	>>> from rhvoice import RHVoice


There are two ways to use it, as direct audio output to be manipulated by you:

.. code::

	>>> audio = RHVoice("Преступление и наказание")
	>>> with open('wav.wav', 'wb') as f:
	...     f.write(audio)

	
Or to be saved by this class:

.. code::

	>>> RHVoice("Дневник писателя", output_file="wave.wav")

Things to do
------------------
1) Test it with Python 2
2) Add to PyPi

As you can see, code base is simple. It can be improved so feel free to suggest patches with new features.


