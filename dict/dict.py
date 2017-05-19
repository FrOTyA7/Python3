D = {} # Define_1
D = {'w':5,'Khalid':7} # Define_2
print('Khalid' in D)  # it return True
D2 = dict( zip(['key','A','B','C'],['value',0,1,2] )) # Define_2
D['w']=55 # Add
print(D) # Print
del D['w'] # Dellete item
print(D)
print(D.items()) # View Items
print(D.keys()) # View Keys
print(D.values()) # View Vlues
D.get('dw','aaaa7a') # if dw is exsist as key it return dw's Value Else return aaaa7a
del D # Dellete the Dect
D2.clear # Clear 
