# Write a python program to find the sum of first n natural number using while loop 
num=int(input("Enter the number: "))
i=1
sum=0
while(i<=num):
    sum=sum+i
    i+=1
print(sum)

# formula for finding the sum of natural number is (num(num+1)/2)