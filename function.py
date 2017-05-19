def get_gender(sex='Unkonwn'):      # function(var='Defult')
 if sex is 'm':
  sex = 'Mail'
 elif sex is 'f':  
   sex = 'femail'
 print(sex)
 
 
get_gender('m')
# mail

get_gender('f')
# Femail

get_gender()
# Unkonwn




#                         mane input to 1 var like list
def add_number(*args):
 print(args)
 
add_number(5)
# (5,)
add_number(5,1)
# (5,1)
add_number(5,1,4,5)
# (5,1,4,5)

#      list[] or set{} or () include function as paramiter
def health_chek(age,apple_ate,smoke):
  answer = (100-age + apple_ate*3 - smoke*2)
  print (answer,"%")
  
khalid_data = [19,5,0]
health_chek(khalid_data[0],khalid_data[1],khalid_data[2])
health_chek(*khalid_data)  # *list = (x,y,z)  *set  
health_chek(19,5,0)