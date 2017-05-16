print ('==> Table Project coded by Khalid <==')

while True:
     try:
         X = int(input("Please enter an integer: "))
         for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
                        print (X ,' X ' , i, ' = ', X*i)
         break
     except ValueError:
                print("Oops!  That was no valid number.  Try again...")

