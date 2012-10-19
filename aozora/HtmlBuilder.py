# -*- coding: utf-8 -*-

import sys
import re

from lib import BeautifulSoup

""" HTML Builder

Module for building the final markup from lists of parsed strings.
"""

_TOP = """
<!DOCTYPE html>
<html>
<head>
  <title></title>
  <meta charset="utf-8">
</head>
<body>
  <div id="container">
"""

_BOTTOM = """
  </div>
</body>
"""


def _paragraph(content):
    """ 
    Builds a paragraph tag for main content.  Returns a linebreak
    for an empty string
    """
    if re.match(ur'^\s*$', content, re.UNICODE):
        return u'<br/>'
    else:
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

def buildHtml(strlist):
    """
    Builds an HTML document from a list of strings parsed by NovelParser.
    """

    # Regexes for identifying markers:
    heading_marker = re.compile(ur'［＃HEADING］', re.UNICODE)
    page_marker    = re.compile(ur'［＃ページ ([0-9]+?)］', re.UNICODE)

    heading_count = 0

    for i, string in enumerate(strlist):

        # Header
        match = heading_marker.match(string)
        if match:
            print "found header %s" % string
            content = string[:match.start()] + string[match.end():]

            heading_count += 1
            strlist[i] = _chapterHead(content, heading_count)

        else:
            # Page break
            match = page_marker.match(string)
            if match:
                print "found pgbreak"
                strlist[i] = _pagebreak(match.group(1))

            else:
                # Standard line
                print "found paragraph"
                strlist[i] = _paragraph(string)


    # Join the main block of content together.
    block = u'\n'.join(strlist)

    rv = _TOP + block + _BOTTOM

    return rv