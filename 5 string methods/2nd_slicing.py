# strng="My name is Gaurav Rajput"

# name=strng[::2]
# # In string slicing [start:stop:step]
# # start=0 by default
# # stop=length of the String 
# # step=1 by default
# g=strng[5:18:3] # In this string will start from 5th index and end 18th index and encrease with 3 

# print(g)
# print(name)

# Exmple of the string slicing 

String1="Kartikchauhna12456"
String2="Vivek45789"
String3="MohanSharma58794"
String4="Varunkumar87945"

# by help of slicing we can et their id very easily
id=String1[-5::1]
print(id)
id2=String2[-5::1]
print(id2)

# for reversing the string 

name="Shanu kumar "
rev=name[::-1]
print(rev)