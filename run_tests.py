#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import sys
import logging

sys.path.append(".")
from tests import parser_tests, ruby_tests
from lib import test_runner


# Suppress log messages on stderr
logging.basicConfig(level = logging.CRITICAL)

# Define test instances: ex:
# log_load = Log_tests.TestLog('test_load')

parser_newlines   = parser_tests.TestParser('test_cleanNewlines')
parser_headings   = parser_tests.TestParser('test_findHeadings')
parser_paragraphs = parser_tests.TestParser('test_parseParagraphs')
parser_pagesplit  = parser_tests.TestParser('test_pageSplit')
parser_parse      = parser_tests.TestParser('test_parse')

ruby_tohtml = ruby_tests.TestRuby('test_toHtml')
ruby_parse  = ruby_tests.TestRuby('test_parseRubytext')

test_suite = test_runner.ModuleTestRunner()

# Add tests to test suite:
# test_suite.addTestList("MODULE NAME", [List, of, tests])
test_suite.addTestList("Parser", [parser_newlines,
                                  parser_paragraphs,
                                  parser_headings,
                                  parser_pagesplit,
                                  parser_parse])

test_suite.addTestList("Ruby", [ruby_tohtml,
                                ruby_parse])

if __name__ == "__main__":
    # Run test suite
    test_suite.run()