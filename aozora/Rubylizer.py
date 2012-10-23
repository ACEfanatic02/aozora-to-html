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

    return u'<ruby class="bouten"><rb>%s</rb><rp>(</rp><rt>%s</rt><rp>)</rp></ruby>'\
            % (kanji, bouten)

def toBousen(kanji):
    """
    Produces a special class of ruby tags for 傍線 marks.
    """
    bousen = u"ー" * len(kanji)

    return u'<ruby class="bousen"><rb>%s</rb><rp>(</rp><rt>%s</rt><rp>)</rp></ruby>'\
            % (kanji, bousen)

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
        """, re.X|re.UNICODE)

    bouten_match = re.compile(ur"(.+?)［＃「\1」に傍点］", re.UNICODE)
    bousen_match = re.compile(ur"(.+?)［＃「\1」に傍線］", re.UNICODE)

    for match in furigana_match.finditer(string):
        kanji = match.group(1).lstrip(u'｜')
        rubytext = match.group(2).strip(u'《》')

        string = string.replace(match.group(), 
            toRuby(kanji, rubytext))

    found_bouten = []
    for match in bouten_match.finditer(string):
        found_bouten.append(match)

    for match in reversed(found_bouten):
        string = string[:match.start()] + toBouten(match.group(1)) +\
            string[match.end():]

    found_bousen = []
    for match in bousen_match.finditer(string):
        found_bousen.append(match)

    for match in reversed(found_bousen):
        string = string[:match.start()] + toBousen(match.group(1)) +\
            string[match.end():]

    return string
