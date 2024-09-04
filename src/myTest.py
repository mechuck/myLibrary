#!/usr/bin/env python
""" Testing File for myLibrary.

This module is a location for testing function within the myLibrary module.
"""

__author__ = "Chuck Nelson"
__copyright__ = "Copyright 2024, myLibrary Project"
__credits__ = ["Chuck Nelson"]

__license__ = "MIT"
__maintainer__ = "Chuck Nelson"
__email__ = "chuck_nelson@hotmail.com"
__status__ = "Prototype"

# Created Date: 09/03/2024

import myLibrary as ml


# Testing the getTimeStamp()
print(f"Current Time Stamp: {ml.getTimeStamp()}")
# Testing the getTimeStampFile()
print(f"Current Time Stamp for File: {ml.getTimeStampFile()}")

# Testing the isBoolFromText() Function
# strTest1 = "True"
# strTest2 = "False"
# print(f"Is Boolean: {ml.isBoolFromText(strTest1)}")
# print(f"Is Boolean: {ml.isBoolFromText(strTest2)}")