#!/usr/bin/env python

import sys
import re

"""
This code should work to parse through a text file (in this case the origin of species)

and return words that relate to heritability. The script should return the line number and the word itself.

Let's see how this goes
"""

def completion_text():
    print('output file should be labelled herit_occurences.txt')


if  __name__ == '__main__':


    parse_pat = "\w*herit\w*"
    # I believe that this pattern should return everything relating to heritability
    parse_obj = re.compile(parse_pat, re.IGNORECASE)


    with open('origin.txt', 'r') as in_stream:
        print('Origin.txt file opened')
        with open('herit_occurences.txt', 'w') as out_stream:
            for line_index, line in enumerate(in_stream, 1):
                if parse_obj.findall(line):
                    match = parse_obj.search(line)
                    out_stream.write("{0}\t{1}\n".format(line_index, match.group()))

    print('Done!')
    print('dummy.txt is closed?', in_stream.closed)
    print('output.txt is closed?', out_stream.closed)

    completion_text()

