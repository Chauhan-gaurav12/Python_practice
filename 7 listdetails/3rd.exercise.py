# 1. Write a program to store seven fruits in a list entered by the user

lis=[]
a=input("Enter the fruits name: ")
lis.append(a)
b=input("Enter the fruits name: ")
lis.append(b)
c=input("Enter the fruits name: ")
lis.append(c)
d=input("Enter the fruits name: ")
lis.append(d)
e=input("Enter the fruits name: ")
lis.append(e)
f=input("Enter the fruits name: ")
lis.append(f)
g=input("Enter the fruits name: ")
lis.append(g)

print(lis)

print("Total fruits name is : ",len(lis))
print("The list 1st index is : ",lis[0])

#By for loop

lis=[]
a=int(input("Enter the range of the list: "))
for i in range(1,a+1):
    a=input("Enter the list value: ")
    lis.append(a)
    i=i+1

print(lis)
print("The length of the string is  : ",len(lis))


