# Top
import sys
orig_stdout = sys.stdout
f = open('out.txt', 'w')



# Code
sys.stdout = f
print ('Code Here')
sys.stdout = orig_stdout



# End
f.close()