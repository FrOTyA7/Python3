
#            Remove  the item that have i index        list.pop([i])    if no i ==> list.pop()  Remove last item     pop
# popleft()

>>> fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

>>> print ( fruits.pop(5) )
'apple'

>>> print ( fruits )
['orange', 'apple', 'pear', 'banana', 'kiwi', 'banana']       # there is no apple that have 5th index

>>> fruits.pop()
>>> print ( fruits )
['orange', 'apple', 'pear', 'banana', 'kiwi']          # there is no last item
