#!/usr/bin/env python3
""" a2txt

    Usage:

        a2txt my_spoken_audio_file.m4a > transcript.txt

    Flags:

    -w This will cause the output to be word-wrapped at 80 characters.

    This script uses OpenAI's whisper model to transcribe your audio file into
    text. This expects that your OpenAI API key is defined in the environment
    variable OPENAI_API_KEY.
"""


# ______________________________________________________________________
# Imports

import argparse
import os
import sys
import textwrap

from openai import OpenAI


# ______________________________________________________________________
# Transcription function

def transcribe_audio_file(filename, do_word_wrap):

    client = OpenAI()

    with open(filename, 'rb') as f:
        transcript = client.audio.transcriptions.create(
                model='whisper-1',
                file=f
        )

    text = transcript.text

    if do_word_wrap:
        print('\n'.join(textwrap.wrap(text, width=80)))
    else:
        print(text)


# ______________________________________________________________________
# Main

if __name__ == '__main__':

    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(0)

    if os.getenv('OPENAI_API_KEY') is None:
        print(__doc__)
        print('\n!! No API key found in the env variable OPENAI_API_KEY !!\n')
        sys.exit(0)

    do_word_wrap = ('-w' in sys.argv)

    if do_word_wrap:
        # The fname is at index 1 or 2; the alternate of the -w index.
        fname = sys.argv[3 - sys.argv.index('-w')]
    else:
        fname = sys.argv[1]

    transcribe_audio_file(fname, do_word_wrap)
