# -*- coding: utf-8 -*-

import re

""" Rubylizer

Module for preparing rubytext tags from the furigana marked in
青空文庫-formatted text.
"""

def toRuby(kanji, rubytext):
    """
    Produce the proper HTML tag given a block of %kanji and its related 
    %rubytext.

    TODO: Attempt to parse rubytext per character:
    例    文
    れい・ぶん
    """

    return u"""<ruby><rb>%s</rb><rp>(</rp><rt>%s</rt><rp>)</rp></ruby>"""\
            % (kanji, rubytext)

def toBouten(kanji, bouten):
    """
    Produces a special class of ruby tags for bouten emphasis marks.
    """

    return u"""<ruby class="bouten"><rb>%s</rb><rp>(</rp><rt>%s</rt><rp>)</rp></ruby>"""\
            % (kanji, bouten)

def parseRubytext(string):
    """
    Identifies furigana from the provided %string, then replaces with the
    proper HTML tag set.
    """
    furigana_match = re.compile(ur"""
        # match block separator (if it exists)
        ([｜]?
        # match and capture kanji
        [々\u3400-\u4DB5\u4E00-\u9FCB\uF900-\uFA6A]+)     
        # match and capture ruby statement
        (《.*?》)
        """, re.X)

    bouten_match = re.compile(ur"""
        ［＃「(.*?)」に傍点］
        """, re.X|re.UNICODE)

    for match in furigana_match.finditer(string):
        kanji = match.group(1).lstrip(u'｜')
        rubytext = match.group(2).strip(u'《》')

        string = string.replace(match.group(), 
            toRuby(kanji, rubytext))

    for match in bouten_match.finditer(string):
        ## BROKEN: need to list and then replace in reverse to keep index accurate ## 
        bouten_count = len(match.group(1))
        bouten_start = match.start() - bouten_count

        kanji = string[bouten_start:match.start()]

        bouten = u"・" * bouten_count

        string = string.replace(string[bouten_start:match.end()],
            toBouten(kanji, bouten))

    return string
