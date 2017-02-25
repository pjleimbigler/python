#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""wordcount.py: Read in a text file as its only parameter. Print
word count, and a sorted list of the most common words along with their
occurrences.
"""

__author__ = 'Peter Leimbigler'
__email__ = 'pjleimbigler@gmail.com'
__date__   = '2017-02-04'
__status__ = 'Prototype'

import sys

# simple but not as good as the option below, for some reason:
# f = open(sys.argv[1], 'r')
# contents = f.read()
# f.close()

# Using the with statement automatically closes the file after reading, no
# matter how the nested block exits.
# File objects expose their own __enter__ and __exit__ methods, and can
# therefore act as their own context managers. Specifically, the __exit__
# method closes the file.
with open(sys.argv[1], 'r') as f:
    contents = f.read()

# Create a list of words, splitting at non-alphanumerics.
words = ''.join(c if (c.isalnum() or c == '\'') else ' ' for c in\
        contents).split()
# Save the word count.
wc = len(words)
# Create a lowercase word list. Python 3.3 adds the unicode-friendly 
# casefold(), enabling ü -> u, ß -> ss, etc. But I wrote this on Python 2.7 and
# will simply accept inaccuracy in case of accents.
wc_lc = [word.lower() for word in words]
# Create a dictionary with keys = words, values = counts.
dct = {word:words.count(word) for word in words}

# sort() sorts in-place. sorted() creates a sorted iterable.
for key, value in sorted(dct.items(), key=lambda x: x[1], \
        reverse=True)[:10]:
    print "%s: %s" % (key, value)

# Before the above, I wrote this:
# for key, value in sorted(dct.iteritems(), key=lambda (k, v): (v, k), \
#       reverse=True)[:10]:
#    print "%s: %s" % (key, value)
