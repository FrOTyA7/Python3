#!/usr/bin/python 
i = 2
while(i < 1000): 
	j = 2 
	while(j <= (i/j)): 
		if not(i%j): break 
		j = j + 1 
	if (j > i/j) : print (i, " is prime") 
	i = i + 1 
 
print ("Good bye!")
######
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')