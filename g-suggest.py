#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import sys

GOOGLE_SUGGEST = "http://suggestqueries.google.com/complete/search?output=toolbar&hl=en&oe=utf8&q="
EXAMPLE_TERM = "不可以"

def getxml(search_term):
    mysuggest = GOOGLE_SUGGEST + urllib2.quote(search_term)

    response = urllib2.urlopen(mysuggest)
    html = response.read()
    return html

def main():
    if  len(sys.argv) != 2:
        print "Need one search term!"
        xml = getxml(EXAMPLE_TERM)
    else:
        print "Get Google suggest queries of " + sys.argv[1]
        xml = getxml(sys.argv[1])

    print xml

if __name__ == '__main__':
    main()

