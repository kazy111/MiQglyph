# -*- coding: utf-8 -*-
import math
import sys
import os
import re

height = 840
# read

# fix top side bearing
pattern = re.compile(r'^    <mtx name="([^"]+)" height="([\-0-9]+)" tsb="([\-0-9]+)"\/>$')
result = ''
f = open('MiQglyph.ttx', 'r')
for line in f:
    matches = pattern.match(line)
    if matches:
        id = matches.group(1)
        em_height = matches.group(2)
        tsb = int(matches.group(3))
        if id == '.notdef':
            tsb = 50
        elif id in {'uni3041', 'uni3043', 'uni3045', 'uni3047', 'uni3049', 'uni3063',
                    'uni3083', 'uni3085', 'uni3087', 'uni30A1', 'uni30A3', 'uni30A5',
                    'uni30A7', 'uni30A9', 'uni30C3', 'uni30E3', 'uni30E5', 'uni30E7'}:
            # small kana
            tsb = height - tsb - 250
        else:
            tsb = height - tsb
        result += '    <mtx name="%s" height="%s" tsb="%s"/>\n' % (id, em_height, str(tsb))
    else:
        result += line
f.close()

# write
f = open('MiQglyph.ttx', 'w')
f.write(result)
f.close()
