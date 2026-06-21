# Write a recursive function to Calculate  the sum  of first natural numbers 
def sum(num):
    sum=0
    for i in range(1,num+1):
        sum=sum+i
    print(f"The sum is {sum}")
num=int(input("Enter the number : "))
sum(num)
