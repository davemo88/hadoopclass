#!/usr/bin/env python

import sys
import re

patterns = sys.argv[1:]

for line in sys.stdin:
    val = line.strip().lower()
    for p in patterns:
        print "%s\t%s" % (p, len(re.findall(p.lower(), val)))