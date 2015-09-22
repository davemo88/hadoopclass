#!/usr/bin/env python
import sys

## to handle key changes
last_key, count = None, 0

for line in sys.stdin:
    (key, val) = line.strip().split('\t')

## when we change keys, emit the k-v pair
## for last key and start counting for new key
    if last_key and last_key!= key:
        print '%s\t%s' % (last_key, count)
        (last_key, count) = (key, int(val))
## in this case the key hasn't changed yet
    else:
        (last_key, count) = (key, (count + int(val)))
## emit the k-v pair for the last key in the input
if last_key:
    print '%s\t%s' % (last_key, count)