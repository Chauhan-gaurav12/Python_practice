# Write a program to accept marks of 6 student and display the in the sorted manner 

lis=[]
a=int(input("Enter the number of student: "))

for i in range(1,a+1):
    marks=int(input("Enter the marks of the student: "))
    lis.append(marks)
    i=i+1
print(lis)
lis.sort()
print("The sorted list is : ",lis)
