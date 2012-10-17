# -*- coding: utf-8 -*-

import sys
import re

from aozora.Rubylizer import parseRubytext

""" Parser

Module for parsing 青空文庫-formatted text into Python strings.  Assumes
UTF-8 input and returns Python unicode literals; makes no attempt to deal
with any other encoding.
"""

class NovelParser(object):

    def __init__(self, pglen=400, heading_regex=ur"^.*[０-９]+$"):
        """ Attributes:
        %pglen : approximate length of one page in characters.
        %heading_regex : unicode regex string for identifying chapter headings.
        """

        object.__init__(self)

        self.pglen = pglen
        self.heading_regex = heading_regex

    def _clense(self, text):
        """
        Standardizes newlines.
        """
        text = re.sub(ur'\r\n', u'\n', text)
        text = re.sub(ur'\r', u'\n', text)
        return text

    def _mark_pages(self, text):
        """
        Inserts comments in %text to mark the end of pages.  Differs from BDH's
        in that it breaks only at newlines or punctuation for a clean result.
        """
        # Regex ripped wholesale from BDH.
        to_skip = re.compile(ur"""((-------------------------------------------------------.*?-------------------------------------------------------)|(｜)|(［＃.*?］)|(《.*?》)|(<.*?>)|(\n)|(\s))+""", re.UNICODE | re.S)

        skipped = []
        for match in to_skip.finditer(text):
            skipped.append(match.span())

        markers = []

        cur_pos = 0
        num_chars = 0
        text_len = len(text)
        next_skip = 0

        while cur_pos < text_len:

            if num_chars % self.pglen == 0 and not \
                (next_skip < len(skipped) and skipped[next_skip][0] == cur_pos):
               
                # Okay, we need a new page: look for the next good breakpoint:
                offset = 0
                while not (text[cur_pos + offset] in u"、。！？!?\n"):
                    
                    # Don't go past EOF            
                    if offset + cur_pos == text_len:
                        break

                    offset += 1

                markers.append(cur_pos + offset)

            to_next_page = self.pglen - (num_chars % self.pglen)
            to_next_skip = sys.maxint

            if next_skip < len(skipped):
                to_next_skip = skipped[next_skip][0] - cur_pos

            if to_next_skip <= to_next_page:

                num_chars += to_next_skip
                cur_pos = skipped[next_skip][1]
                next_skip += 1

            else:
                num_chars += to_next_page
                cur_pos += to_next_page

        # Now, actually insert the page markers
        for index, pos in enumerate(reversed(markers)):
            text = text[:pos] + u"［＃ページ " + str(
                len(markers) - index) + u"］" + text[pos:]

        return text

    def _mark_headings(self, text):
        """
        Inserts comments to mark chapter headings.
        """
        heading_marker = u"［＃HEADING］"
        headings = []

        for match in text.finditer(self.heading_regex):
            headings.append(match.start)

        for index, pos in enumerate(reversed(headings)):
            text = text[:pos] + heading_marker + text[pos:]

        return text

    def parse(self, raw_text):
        """
        Parse the %raw_text into a list of strings.
        """
        raw_text = self._clense(raw_text)

        raw_text = self._mark_pages(raw_text)
        raw_text = self._mark_headings(raw_text)

        # Split lines
        strlist = raw_text.split('\n')

        # Convert rubytext
        for string in strlist:
            string = parseRubytext(string)

        return strlist
