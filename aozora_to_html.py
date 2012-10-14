#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Aozora To HTML

A suite of tools to turn 青空文庫-formatted text into an easily readable HTML
document.  The goal is to create a format that is comfortable to read, even on
a computer screen.

TOOLS:
-- 1. Rubificator
    
    Turns 青空文庫 furigana into actual ruby tags (supported natively in Chrome,
    and via extensions in Firefox.)

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

import lib.BeautifulSoup

import aozora
