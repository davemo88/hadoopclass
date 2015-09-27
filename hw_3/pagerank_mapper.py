#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.split()
    key = line[0]
    outlinks = line[1:-1]
    pr = line[-1]
    for outlink in outlinks:
        print '%s\t%s' % (outlink, float(pr)/len(outlinks))
## output the outlinks
    print '%s\t%s' % (key, ' '.join(outlinks))