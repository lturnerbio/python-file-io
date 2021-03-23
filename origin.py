#!/usr/bin/env python

import sys
import re 

"""
This code should work to parse through a text file (in this case the origin of species)

and return words that relate to heritability. The script should return the line number and the word itself.

Let's see how this goes
"""

#if  __name__ == '__main__'

parse_pat = "\w*herit\w*"

