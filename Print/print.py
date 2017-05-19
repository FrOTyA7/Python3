print ( value1 [start:end:step], value2 [::], '....' , sep=' ' , end='\n' , file=sys.stdout , flush=false )

#    sep what between << value1 and value2  >>

>>> print('foo', 'bar')
foo bar
>>> print('foo', 'bar', sep='')
foobar
>>> print('foo', 'bar', sep=' -> ')
foo -> bar

#      end the end of line 

>>> print('foo')
>>> print('bar')
foo
bar
>>> print('foo',end='')
>>> print('bar')
foobar

# to reverce print
print('khalid'[::-1])


print('khalidx'[::])
#      0123456
#     - 654321


