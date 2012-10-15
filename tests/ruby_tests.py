# -*- coding: utf-8 -*-

import unittest
import sys

sys.path.append('..')
from aozora.Rubylizer import Rubylizer

class TestRuby(unittest.TestCase):

    def test_toHtml(self):

        self.assertEquals(u"<ruby><rb>Kanji</rb><rp>(</rp><rt>Ruby</rt><rp>)</rp></ruby>",
            Rubylizer.toHtml(u"Kanji", u"Ruby"))

    def test_parseRubytext(self):

        single_ruby_data = u"「阿良々木《あららぎ》先輩、待たせてしまって申し訳ない」"
        multi_ruby_data  = u"千石《せんごく》撫子《なでこ》は妹の同級生だった。"

        single_ruby_expect = u""
        multi_ruby_expect  = u""