#!/usr/bin/env python
# 2017-1-31 Tue  Peter Leimbigler
# Play around with python dictionaries. Learn how to use them.
# Also use the map() function. I should probably be writing docstrings...

dct =  {'Heather':'Doig', 'Peter':'Leimbigler', 'Barack':'Obama',
        'Betsy':'Leimbigler'}

print 'print dct output:'
print dct

print 'print dct.iteritem() output:'
print dct.iteritems()

print 'Now looping over each key in dct...'
for key in dct:
    print 'The last name of', key, 'is', dct[key]

print 'Now let\'s loop over each key-value pair in dct.iteritems()...'
for key, value in dct.iteritems():
    print 'The first name of', value, 'is', key

print 'Now, let\'s use a generator expression to find the first key for a \
given value:'

# Generator expression iterates only as far as needed to return the first
# value. This raises a StopIteration exception if no match is found.
try:
    first_name_of_leimbigler = \
        (key for key, value in dct.iteritems() if value == 'Leimbigler').next()
    print first_name_of_leimbigler
except StopIteration:
    print "The requested value could not be found."

while True:
    lastname_user = raw_input('Please type a last name: ')
    try:
        first_name = (key for key, value in dct.iteritems() if \
                value == lastname_user).next()
        print 'The first person I found with the last name {} is {}.'.\
                format(lastname_user, first_name)
    except StopIteration:
        print 'Nobody with the last name {} was found in the dictionary.'.\
                format(lastname_user)
#    except KeyboardInterrupt:
    except:
        print 'Goodbye.'
