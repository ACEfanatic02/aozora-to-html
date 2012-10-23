# -*- coding: utf-8 -*-

import unittest
import sys

sys.path.append('..')
import aozora.Rubylizer as Rubylizer

class TestRuby(unittest.TestCase):

    def test_toRuby(self):

        self.assertEquals(u"<ruby><rb>Kanji</rb><rp>(</rp><rt>Ruby</rt><rp>)</rp></ruby>",
            Rubylizer.toRuby(u"Kanji", u"Ruby"))

    def test_parseRubytext(self):

        single_ruby_data = u"「阿良々木《あららぎ》先輩、待たせてしまって申し訳ない」"
        multi_ruby_data  = u"千石《せんごく》撫子《なでこ》は妹の同級生だった。"

        single_ruby_expect = u"「<ruby><rb>阿良々木</rb><rp>(</rp><rt>あららぎ</rt><rp>)</rp></ruby>先輩、待たせてしまって申し訳ない」"
        multi_ruby_expect  = u"<ruby><rb>千石</rb><rp>(</rp><rt>せんごく</rt><rp>)</rp></ruby><ruby><rb>撫子</rb><rp>(</rp><rt>なでこ</rt><rp>)</rp></ruby>は妹の同級生だった。"

        self.assertEquals(single_ruby_expect,
            Rubylizer.parseRubytext(single_ruby_data))
        self.assertEquals(multi_ruby_expect,
            Rubylizer.parseRubytext(multi_ruby_data))

    def test_bouten(self):

        single_bouten_data = u"おかしなことはつきもの［＃「つきもの」に傍点］だ"
        multi_bouten_data  = u"激しい運動［＃「運動」に傍点］とか言うのならまだしも、活動［＃「活動」に傍点］を禁じられている"

        single_bouten_expect = u"""おかしなことは<ruby class="bouten"><rb>つきもの</rb><rp>(</rp><rt>・・・・</rt><rp>)</rp></ruby>だ"""
        multi_bouten_expect  = u"""激しい<ruby class="bouten"><rb>運動</rb><rp>(</rp><rt>・・</rt><rp>)</rp></ruby>とか言うのならまだしも、<ruby class="bouten"><rb>活動</rb><rp>(</rp><rt>・・</rt><rp>)</rp></ruby>を禁じられている"""

        self.assertEquals(single_bouten_expect,
            Rubylizer.parseRubytext(single_bouten_data))
        self.assertEquals(multi_bouten_expect,
            Rubylizer.parseRubytext(multi_bouten_data))

    def test_bousen(self):

        bousen_data = u"「あんなこと［＃「あんなこと」に傍線］やこんなこと［＃「こんなこと」に傍線］もしてみたかったわね」"

        bousen_expect = u'「<ruby class="bousen"><rb>あんなこと</rb><rp>(</rp><rt>ーーーーー</rt><rp>)</rp></ruby>や<ruby class="bousen"><rb>こんなこと</rb><rp>(</rp><rt>ーーーーー</rt><rp>)</rp></ruby>もしてみたかったわね」'

        self.assertEquals(bousen_expect,
            Rubylizer.parseRubytext(bousen_data))