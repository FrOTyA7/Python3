import sys
orig_stdout = sys.stdout
pytho = open('next.py', 'w')
print ('==> TaWaFik Project coded by Khalid <==' + '\n')

number = set()
el = 'Khalid'

while (el != 'end' and el != 'End' and el != 'END'):
  number.add(el)
  el = str(input('Type Element(s) then Type End :'))
else:
  number=list(number)
  number.remove("Khalid")
  number.sort()
  
while True:
    try:
         
        
        boxs = int(input('Inter boxs :'))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

#

sys.stdout = pytho
print ('\n#\n#\n#\n')

print ('''import sys
orig_stdout = sys.stdout
f = open('out.txt', 'w')
''')
print ('number = ',end='')
print (number)
print ('boxs = ',end='')
print (boxs)

print('\n'+'\n'+'\n'+'\n')


space = ' '
print ('def boxs' + str(boxs) +'():')

print (3*space + 'possibilities = 0')
print (3*space + r"print ('Working...\n')")
for i in range(0,boxs):
  print( (i+3) *space + r'for n' + str(i+1) + r' in range(0,len(number)):')


print( (boxs+3) *space + 'if ',end='')
print ('n1 == n2 ',end='')
for i33 in range(2,boxs):
  print( ' or n' + str(i33) + ' == n' + str(i33+1) ,end='' )
print (' :') 
print ((boxs+4) *space + 'continue')
print ( (boxs+3) *space + 'sys.stdout = f')
print ( (boxs+3) *space + 'print ( number[n1]',end = '')
for i2 in range(2,boxs+1):
  print (  ('+number[n' + str(i2)) + ']' ,end = '')
print (' )')
print( (boxs+3) *space + 'sys.stdout = orig_stdout')
print( (boxs+3) *space + 'possibilities = possibilities + 1')

print (3*space + r"print ('Number of possibilities is ' , possibilities )" )

print ('\n#\n#\n#\n')

print('\n'+'\n'+'\n'+'\n')

print ('boxs'+ str(boxs) +'()')
print ('f.close()')

sys.stdout = orig_stdout

#

pytho.close()
import next

