# 1. Write a program using function to find gratest of three number 
def greatest(a,b,c):
    if a>b and  a>c:
        print(f"{a} is greater from {b} and {c}")
    elif b>c and b>a:
        print(f"{b} is greater from {a} and {c}")
    else:
        print(f"{c} is greater from {a} and {b}")

a=int(input("Enter the number : "))
b=int(input("Enter the number : "))
c=int(input("Enter the number : "))

greatest(a,b,c)