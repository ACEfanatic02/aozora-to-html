# -*- coding: utf-8 -*-

import unittest
import sys

sys.path.append('..')
from aozora import Parser

class TestParser(unittest.TestCase):

    def test_cleanNewlines(self):

        self.assertEqual(u"Line One\nLine Two",
            Parser.cleanNewlines(u"Line One\r\nLine Two"))
        self.assertEqual(u"Line One\n\nLine Two",
            Parser.cleanNewlines(u"Line One\n\nLine Two"))

    def test_findHeadings(self):

        testdata = u"""
最終話　つきひフェニックス

　００１

　阿良々木月火《あららぎつきひ》の正体を開示することによって、それではいよいよ僕達の物語に終止符を打つことにしよう。あの小賢しくも小うるさい、ちっちゃいほうの妹の話で、僕と、僕の愛すべき仲間たちのエピソードは完結だ。とは言うものの、勿論《もちろん》それで人生が終わるわけじやないし、世界が終わるわけでもない。
　どうしたところで命まで取られるわけじゃあるまいし――大体、終わりのある人生や終わりのある世界が、どれほど救済的なのか、僕達はそのことに、普段からもっと思いを馳《は》せるべきだろう。終わりたくても終われない、やめたくてもやめられない、そんな地獄《じごく》を人間は日常的に、あるいは異常的に、当たり前のように経験し、当たり前のように継続しているはずではないか。

This is not a ００１ heading 
        """

        paragraphs = Parser.parseParagraphs(testdata)
        headingslist = Parser.findHeadings(paragraphs)

        self.assertEqual(headingslist, [1])

    def test_parseParagraphs(self):

        self.assertEqual([u"Paragraph One", u"Paragraph Two"],
            Parser.parseParagraphs(u"Paragraph One\nParagraph Two"))
        self.assertEqual([u"Paragraph One", u"Paragraph Two"],
            Parser.parseParagraphs(u"Paragraph One\n\nParagraph Two"))
        self.assertEqual([u"Paragraph One", u"Paragraph Two"],
            Parser.parseParagraphs(u"Paragraph One\n \nParagraph Two"))
        self.assertEqual([u"Paragraph One", u"Paragraph Two"],
            Parser.parseParagraphs(u"Paragraph One\n\n\nParagraph Two"))

    def test_pageSplit(self):
        
        testdata = u"""
This is the first page.
And this is too.
［＃改ページ］
Second page.
12345678901234567890
12345678901234567890
12345678901234567890
12345678901234567890
12345678901234567890
12345678901234567890
12345678901234567890
12345678901234567890
12345678901234567890
12345678901234567890
12345678901234567890
12345678901234567890
12345678901234567890
12345678901234567890
12345678901234567890
12345678901234567890
12345678901234567890
12345678901234567890
1234567890
This should be page three.
［＃改ページ］

This should be page four.
"""
        
        paragraphs = Parser.parseParagraphs(testdata)
        pages = Parser.pageSplit(paragraphs)

        self.assertEqual(pages[0][0], u"This is the first page.")
        self.assertEqual(pages[1][0], u"Second page.")
        self.assertEqual(pages[2][0], u"This should be page three.")
        self.assertEqual(pages[3][0], u"This should be page four.")

    def test_parse(self):

        testdata = u"""
﻿化物語（上）
西尾維新

<img src="img/a001_s.jpg">
<img src="img/a004_s.jpg">
<img src="img/bakemono0003_s.jpg">
<img src="img/bakemono0004_s.jpg">
<img src="img/bakemono0005_s.jpg">
<img src="img/bakemono0006_s.jpg">
<img src="img/bakemono0007_s.jpg">
<img src="img/bakemono0008_s.jpg">
<img src="img/bakemono0009_s.jpg">
［＃改ページ］
化バケモノ物ガタリ語　上
西尾維新NISIOISIN

阿良々木《あららぎ》暦《こよみ》を目がけて空から降ってきた女の子・戦場《せんじょう》ヶ｜原《はら》ひたぎには、およそ体重と呼べるようなものが、全くと言っていいほど、なかった――!?
台湾から現れた新人イラストレーター、〝光の魔術師〟ことＶＯＦＡＮと新たにコンビを組み、あの西尾維新が満を持して放つ、これぞ現代の怪異！　怪異！　怪異！
青春に、おかしなことはつきもの［＃「つきもの」に傍点］だ！
［＃改ページ］
BOOK&BOX DESIGN VEIA
FONT DIRECTION
SHINICHIKONNO
(TOPPAN PRINTING CO.,LTD)
ILLUSTRTION
VOFAN

本文使用書体：FOT-筑紫明朝ProL
［＃改ページ］
第一話　ひたぎクラブ
第二話　まよいマイマイ
第三話　するがモンキー
［＃改ページ］

［＃改ページ］
第一話　ひたぎクラブ
［＃改ページ］
"""
        print Parser.parse(testdata)