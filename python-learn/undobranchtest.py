#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""undobranchtest.py: A hodgepodge collection of placeholder Python code on
which to test vim's undo branches, and how to recover from accidental ctrl+U.
This also serves as a testbed for vim folding.
"""

# I should probably leave this metadata stuff to git.
__author__ = 'Peter Leimbigler'
__date__ = '2017-02-05'

import random

rand_list = random.sample(xrange(5,13),13-5)
for x in rand_list:
    print x

# A comment.
# Another comment.
# A third comment.
# Change 1.
# Change 2.
# This is change 3.
