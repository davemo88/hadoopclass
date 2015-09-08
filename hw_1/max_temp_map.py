#!/usr/bin/env/python

import sys
import re

for line in sys.stdin:
	val = line.strip()
	(year, temp, q) = (val[0:4], val[4:9], val[9:])
	if (temp != "+9999" and re.match('[01459]', q)):
		print "%s\t%s" % (year, temp)
