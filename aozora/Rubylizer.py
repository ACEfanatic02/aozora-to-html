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

def toBouten(kanji):
    """
    Produces a special class of ruby tags for 傍点 emphasis marks.
    """
    bouten = u"・" * len(kanji)

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

    bouten_match = re.compile(ur"［＃「(.*?)」に傍点］", re.UNICODE)

    for match in furigana_match.finditer(string):
        kanji = match.group(1).lstrip(u'｜')
        rubytext = match.group(2).strip(u'《》')

        string = string.replace(match.group(), 
            toRuby(kanji, rubytext))

    found_bouten = []

    for match in bouten_match.finditer(string):
        bouten_start = match.start() - len(match.group(1))
        print str(match.start() - bouten_start) + u"|" + match.group(1)

        found_bouten.append((bouten_start, match.start(), match.end()))

    for first, mstart, mend in reversed(found_bouten):

        string = string[:first] + toBouten(match.group(1)) + string[mend:]

    return string
