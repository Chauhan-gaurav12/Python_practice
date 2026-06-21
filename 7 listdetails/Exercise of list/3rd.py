# Write  a program to sum of a list with 4 numbers

lis=[]
a=int(input("Enter the number of digit that you want to add:"))

for i in range (1,a+1):
    num=int(input("Enter the number: "))
    lis.append(num)
    i=i+1

print(lis)
print("Sum of the list is: ",sum(lis))