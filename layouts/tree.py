#!/usr/bin/env python

import sys

out = open('tree-' + sys.argv[1] + '-' + sys.argv[2] + '.json', "w")

spacing = 0.4  # m
strips = int(sys.argv[1])
pixels = int(sys.argv[2])
lines = []
for strip in range(0, 16):
    for led in range(-(pixels / 2), pixels / 2):
        lines.append('  {"point": [%.2f, %.2f, %.2f]}' %
                 (strip*spacing, 0, led*spacing))
out.write('[\n' + ',\n'.join(lines) + '\n]')
