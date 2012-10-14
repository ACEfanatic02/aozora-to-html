#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import sys
import logging

sys.path.append(".")
from tests import # Tests go here
from lib import test_runner


# Suppress log messages on stderr
logging.basicConfig(level = logging.CRITICAL)

# Define test instances: ex:
# log_load = Log_tests.TestLog('test_load')

test_suite = test_runner.ModuleTestRunner()

# Add tests to test suite:
# test_suite.addTestList("MODULE NAME", [List, of, tests])

if __name__ == "__main__":
    # Run test suite
    test_suite.run()