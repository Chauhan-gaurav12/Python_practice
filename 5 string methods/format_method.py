# name="Gaurav"
# place="Dhampur"
# b="My name is {}.And i am form {}"
# print(b.format(name,place)) # format will send the name and address in the b

# use of strip function
# str="        ***gaurav***   -------"
# print(str)
# print(str.strip(" ,*,-")) # it will not change in real str


# ljust---  ljust is use to align with at a specfic symbol or space
a="Gaurav"
# x=a.ljust(20,"$") 
# print(x,"is a good boy")

#rjust --- return a right justified version of the string
age=50
b=a.rjust(15,"@")
print(b," is gppd ")