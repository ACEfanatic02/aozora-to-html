#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Aozora To HTML

A suite of tools to turn 青空文庫-formatted text into an easily readable HTML
document.  The goal is to create a format that is comfortable to read, even on
a computer screen.

TOOLS:
-- 1. Rubylizer
    
    Turns 青空文庫 furigana into actual ruby tags (supported natively in Chrome,
    and via extensions in Firefox.)

"""

__metadata__ = """
Author:     ACEfanatic02 (acefanatic02@gmail.com)
Credits:  - Jeremy Davidson (BlackDragonHunt) -- for the original suite
            of Tadoku Tools on which this project is based.
          - Brian Nez (thedude@bri1.com) -- for 'pretty.py', used for color in 
            the testing suite.
          - Uses BeautifulSoup for HTML processing.
Disclaimer: No warranty, provided 'as-is', etc.  Thou shalt not blame me if 
            this script breaks or damages your machine or data.
"""

import sys
import os.path
import codecs
import logging

from lib import BeautifulSoup

from aozora import Parser, Rubylizer

HELP_USAGE = """USAGE:
$ python aozora_to_html.py <filename>

Will output to directory ./<filename>/ .  Will overwrite any existing files on
name conflict.
"""

def help():
    print HELP_USAGE
    sys.exit()

def loadFile(filename):
    """
    Loads file at %filename as utf-8 and returns it as a unicode object (using
    BeautifulSoup's UnicodeDammit class.)
    """
    try:
        with codecs.open(filename, 'r', encoding=codecs.UTF8) as f:
            rv = f.read()
            f.close()
            return BeautifulSoup.UnicodeDammit(rv).unicode
    except IOError, e:
        logging.error("ERROR - File load failed: %s" % str(e))
        return None

def main(argv):
    pass

if __name__ == '__main__':
    main(sys.argv)
