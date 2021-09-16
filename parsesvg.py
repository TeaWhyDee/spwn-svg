#!/usr/bin/python3

from svgelements import *
import numpy

offset = 0
input_svg = "resources/svg.svg"

import getopt
import sys

argv = sys.argv[1:]
opts, args = getopt.getopt(argv, 'o:offset:i:input')

for o, a in opts:
    if o in ("-o", "--offset"):
        offset = int(a)
    elif o in ("-i", "--input"):
        input_svg = a
    else:
        assert False, "unhandled option"


file = open(input_svg)
svg = SVG.parse(file)

f = open("resources/res_lines.spwn", "w")
string = 'return ['
polylines = []
for e in svg.elements():
    if isinstance(e, Polyline) and len(e) > 1:
        segments = []
        for i in range(len(e) - 1):
            offsetvector = numpy.array([e[i+1].x - e[i].x, e[i+1].y - e[i].y])
            offsetvector = offsetvector / numpy.linalg.norm(offsetvector) * offset
            print(offsetvector)
            segment = []
            segment.append(e[i].x - offsetvector[0])
            segment.append(e[i].y - offsetvector[1])
            segment.append(e[i+1].x + offsetvector[0])
            segment.append(e[i+1].y + offsetvector[1])
            segments.append(segment)
        polylines.append(segments)

string = "return " + str(polylines)

print(string)

f.write(string)
