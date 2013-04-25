#!/usr/bin/env python
# -*- coding: utf-8 -*
import urllib2

GOOGLE_SUGGEST = "http://suggestqueries.google.com/complete/search?output=toolbar&hl=en&oe=utf8&q="

mysuggest = GOOGLE_SUGGEST + "RTFM"

response = urllib2.urlopen(mysuggest)
html = response.read()
print html
