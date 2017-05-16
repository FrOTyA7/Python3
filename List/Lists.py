>>> list(range(5))
[0, 1, 2, 3, 4]

#

print (range(5))
range(0, 5)

#                                                                 List of Numbers

>>> squares = [1, 4, 9, 16, 25]
>>> cubes = [1, 8, 27, 64, 125]
>>> squares
[1, 4, 9, 16, 25]

#
#
#
#                                                              List Of Letters  Remember 'a' 'b'

>>> letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> letters
['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> # replace some values
>>> letters[2:5] = ['C', 'D', 'E']
>>> letters
['a', 'b', 'C', 'D', 'E', 'f', 'g']
>>> # now remove them
>>> letters[2:5] = []
>>> letters
['a', 'b', 'f', 'g']
>>> # clear the list by replacing all the elements with an empty list
>>> letters[:] = []
>>> letters
[]

#
#
#                                                            Print a part of List

>>> squares[0]  # indexing returns the item
1
>>> squares[-1]
25
>>> squares[-3:]  # slicing returns a new list
[9, 16, 25]
#
#
>>> squares[:]
[1, 4, 9, 16, 25]

#
#
#
#
#                                                    create lists containing other lists

>>> a = ['a', 'b', 'c']
>>> n = [1, 2, 3]
>>> x = [a, n]

>>> x
[['a', 'b', 'c'], [1, 2, 3]]

>>> x[:]
[['a', 'b', 'c'], [1, 2, 3]]

>>> x[0]
['a', 'b', 'c']

>>> x[1]
[1, 2, 3]

>>> x[0][1]                         # Print the [1] one of the [0] of x list --->     x[0]-->['a', 'b', 'c']  '(< x[0] >)'[1] --> b
b