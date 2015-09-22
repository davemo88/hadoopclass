#!/usr/bin/env python

import sys
import re

## pass the patterns to be matched as positional arguments to this script
patterns = sys.argv[1:]

for line in sys.stdin:
## note input and patterns are both sent to lower case
## for case insensitive matching
    val = line.strip().lower()
    for p in patterns:
## count the number of times each pattern appears in the input
        print "%s\t%s" % (p, len(re.findall(p.lower(), val)))