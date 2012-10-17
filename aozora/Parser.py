# -*- coding: utf-8 -*-

import re

""" Parser

Module for parsing 青空文庫-formatted text into Python strings.  Assumes
UTF-8 input and returns Python unicode literals; makes no attempt to deal
with any other encoding.
"""
RE_EMPTY = ur'^[ \t\r\f\v]*$' # \s doesn't match empty unicode properly

def cleanNewlines(raw):
    """ 
    Standardizes newlines in %raw. Does not remove extra newlines. 
    """
    return re.sub(ur'\r\n', u'\n', raw)

def findHeadings(strlist):
    """
    Finds anything that looks like a chapter heading in a list of strings
    and returns a list of their indicies.
    """
    rv = []

    for i in range(len(strlist)):
        string = strlist[i]

        heading = re.match(ur"^.*[０-９]+$", string)
        if heading:
            rv.append(i)

    return rv

def parseParagraphs(raw):
    """
    Parses paragraphs into a list of unicode strings.  Does not return
    empty strings.
    """
    rv = []
    raw = cleanNewlines(raw)

    split = raw.split(u'\n')
    for paragraph in split:
        if not re.search(paragraph, RE_EMPTY):
            rv.append(paragraph)

    return rv

def pageSplit(strlist):
    """
    Takes a list of strings, returns a nested list in blocks of ~400
    characters. (One Tadoku page.)
    """
    forced_pgbreak = re.compile(ur"［＃改.*?］")

    pages = []

    cur_page  = []
    cur_pglen = 0

    for string in strlist:

        if forced_pgbreak.match(string):
            if len(cur_page) > 0:
                cur_page.append(string)
            pages.append(cur_page)
            cur_page  = []
            cur_pglen = 0

        elif cur_pglen + len(string) < 400:
            cur_page.append(string)
            cur_pglen += len(string)

        else:
            pages.append(cur_page)
            cur_page  = [string]
            cur_pglen = len(string)

    # Append the final page
    pages.append(cur_page)

    return pages

def parse(raw):
    pass
    

