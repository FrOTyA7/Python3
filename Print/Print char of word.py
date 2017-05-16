
#         +---+---+---+---+---+---+
#         | P | y | t | h | o | n |
#         +---+---+---+---+---+---+
#         0   1   2   3   4   5   6
#         -6  -5  -4  -3  -2  -1
#

>>> word = 'Python'

#

>>> print ( word[0] )  # character in position 0
'P'
>>> print ( word[5] )  # character in position 5
'n'

#
#

>>> print ( word[-1] )  # last character
'n'
>>> print ( word[-2] )  # second-last character
'o'
>>> print ( word[-6] )
'P'

#
#

>>> print ( word[0:2] )  # characters from position 0 (included) to 2 (excluded)
'Py'
>>> print ( word[2:5] )  # characters from position 2 (included) to 5 (excluded)
'tho'

#
#

>>> print ( word[:2] )   # character from the beginning to position 2 (excluded)
'Py'
>>> print ( word[2:] )
'thon'
>>> print ( word[-2:] )  # characters from the second-last (included) to the end
'on'
>>> print ( word[:2] + word[2:] )
'Python'
>>> print ( word[4:] )   # characters from position 4 (included) to the end
'on'
>>> print ( word[:4] + word[4:] )
'Python'

#
#

>>> print ( 'J' + word[1:] )
'Jython'
>>> print ( word[:2] + 'py' )
'Pypy'

#
#

>>> print ( word[:] )
'Python'

