
#          Sort the items of the list in place              list.sort(key=None, reverse=False)        sort

>>> Numbers = ['0', '2', '1', '3', '4', '5', '6']

>>> Numbers.sort(reverse=True)
>>> print ( Numbers )
['6', '5', '4', '3', '2', '1', '0']

>>> Numbers.sort(reverse=False)
>>> print ( Numbers )
['0', '1', '2', '3', '4', '5', '6']

#

>>> fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

>>> fruits.sort()
>>> print ( fruits )
['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']

>>> fruits.sort(reverse=True)
>>> print ( fruits )
['pear', 'orange', 'kiwi', 'banana', 'banana', 'apple', 'apple']
