# -*- coding: utf-8 -*-

import sys
import re

from lib import BeautifulSoup

""" HTML Builder

Module for building the final markup from lists of parsed strings.
"""
def _paragraph(content):
    """ 
    Builds a paragraph tag for main content.
    """
    return u'<p class="pg">%s</p>' % (content)

def _chapterHead(content, id):
    """
    Builds HTML for a chapter heading with the given %id for linking from TOC.
    """
    return u'<h3 id="%s" class="chapter_head">%s</h3>' % (id, content)

def _tocLink(label, id):
    """
    Builds an anchor link to the heading with a given %id.
    """
    return u'<a href="#%s">%s</a>' % (id, label)

def _pagebreak(pagenumber):
    """
    Builds markup for the end of a given page.
    """
    return u'''<hr/>
<p id="page%s" class="pagenumber">%s</p>''' % (pagenumber, pagenumber)

def buildAll(pages):
    """
    Converts a nested list of strings in %pages into a collection of HTML
    documents.
    """
    pass
