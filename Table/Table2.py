print ('==> Table2 Project coded by Khalid <==')
Numper = int(input("Please enter an integer: "))
TableRange = int(input("Please enter a Table range: ")) + 1
for i in range(1, TableRange):
     print ( " ", Numper, ' X ', i, ' = ', Numper*i )

#
#                           Range
#              ----------------------------
#     range(X, Y, Z)          range ( Start? , End? , Step? )
#          X => Start
#          Y => End
#          Z => Step
#              ----------------------------
#                     default values
#                            X => 0
#                            Z => 1
#              ----------------------------
#              print (   list( range(X, Y, Z ) )   )

