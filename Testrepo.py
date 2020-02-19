# -*- coding: utf-8 -*-
"""
Updated Feb 19, 2020
The primary goal of this file is to demonstrate a simple unittest implementation

@author: rzhong2
"""

import unittest

from get_repo import get_repos

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class Testrepo(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(get_repos('rzhong2'),'TRUE')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

