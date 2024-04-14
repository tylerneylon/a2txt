# a2txt

*A command-line tool to transcribe audio files into text*

This script uses OpenAI's whisper model to convert your audio files into plain
text, printing the transcript to stdout.

I use this script with audio files from Apple's Voice Memos app. You can gain
access to the `m4a` files by opening the non-mobile version of the app and
dragging the panel for your voice note (the panel
that contains the voice memo title, on the left side) into Finder.

This script assumes you have an OpenAI API key, and that you've been kind enough
to place that key in your `OPENAI_API_KEY` environment variable.

## Installing

```
git clone https://github.com/tylerneylon/a2txt.git
ln $(cd a2txt; pwd)/a2txt.py /usr/local/bin/a2txt
```

## Usage

Example:

        a2txt -w my_spoken_audio_file.m4a > transcript.txt

## Flags

The `-w` flag will cause the output to be word-wrapped at 80 characters.
Otherwise it's a rambling newline-free one-liner, my friend.

