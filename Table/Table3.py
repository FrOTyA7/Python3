print ('==> Table3 Project coded by Khalid <==')
while True:           # loooooooooop ecen break
     try:
         Numper = float(input("Please, enter a Numper: "))
         Start = float(input("Start : "))
         End = float(input("End : ")) + 1
         Step = float(input("Step : "))

    # Convert int float to int

         if Numper % 1 == 0:
          Numper = int(Numper)

 
         import numpy as Range
         for i in Range.arange(Start, End, Step ):

    # Convert int float to int

          if i % 1 == 0:
           i = int(i)

          Eq = float(Numper*i)
          if Eq % 1 == 0:
           Eq = int(Eq)

          print ( " ", Numper, ' X ', i, ' = ', Eq )
         break
     except ValueError:
         print("Oops!  That was no valid number.  Try again...")



#
#                           Float_Range
#            --------------------------------------


#    => numpy is module and it name is => Range and it attribute is => .arange
#            --------------------------------------


#                           Try_Catch
#  while True:
#    try:
#        code include Errors
#        break => Thes to stop trying
#    except => kind Error:
#        print("Message")
