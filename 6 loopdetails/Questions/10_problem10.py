# Write a program to print multiplication table of n using for loop in the reversed order 

num=int(input("Enter the number: "))
i=num*10
while(i>=num):
    print(i)
    i-=num
    