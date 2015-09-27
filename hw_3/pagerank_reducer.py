#!/usr/bin/env python
import sys

## to handle key changes
last_key, outlinks, pagerank = None, [], 0

for line in sys.stdin:
    key, val = line.strip().split('\t')
## when we change keys, emit the k-v pair
## for last key and start counting for new key
    if last_key and last_key!= key:
        print '%s %s %s' % (last_key, outlinks, pagerank)
        last_key, outlinks, pagerank = key, [], 0
    elif last_key == None:
        last_key = key

    try:
## sum the pagerank scores
        pagerank += float(val)
## can't be summed => it's the outlinks
    except ValueError:
        outlinks = val

## emit the k-v pair for the last key in the input
if last_key:
    print '%s %s %s' % (last_key, outlinks, pagerank)