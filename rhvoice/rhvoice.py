#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    RHVoice bindings for Python
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2013 Anton Vlasenko
    :license: MIT License (Expat). See http://www.debian.org/legal/licenses/mit for details.
"""

from subprocess import Popen, PIPE, STDOUT, check_call

DEVNULL = open('/dev/null', 'w') # Silent output
# Checking for RHVoice system installation
try:
    check_call(["RHVoice", "--help"], stdout=DEVNULL)
except OSError as e:
    DEVNULL.close()
    print ("Cannot run RHVoice, make sure RHVoice is \
             installed and accessible for current user. Error message: %s" % e)
    raise
DEVNULL.close()


class RHVoice(object):
    """RHVoice bindings for Python. 

        >>> from python-rhvoice import RHVoice

        There are two ways to use it, as direct audio output to be manipulated
        by you:

        >>> audio = RHVoice("Преступление и наказание")
        >>> with open('wav.wav', 'wb') as f:
        ...     f.write(audio)

        Or to be saved by this class:

        >>> RHVoice("Дневник писателя", output_file="wave.wav")

        @param text_to_pronounce - text string to pronounce by RHVoice.
        @param output_file (optional) - path to save output sound.

    """

    def __new__(cls, text_to_pronounce, output_file=None):
        try:
            p = Popen(['RHVoice'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
        except OSError:
            print ("Cannot create new process for RHVoice")
            raise
        audio = p.communicate(input=text_to_pronounce)[0]

        # TODO: Here can be made some coding to Lame etc: "lame -V 5"

        # If output file not provided: we are returning audio in bytes
        if output_file is None:
            return audio
        else:
            cls.save_to_file(audio, output_file)
            return None

    @classmethod
    def save_to_file(cls, data, file_path):
        # We have to write by ourselves.
        try:
            f = open(file_path, 'wb')
        except IOError as e:
            print ("Cannot open file with provided file name: %s" % e)
            raise

        # Writing audio bytes into opened file
        try:
            f.write(data)
        except IOError as e:
            print ("Cannot write audio track into opened file: %s" % e)
            raise
        finally:
            f.close()