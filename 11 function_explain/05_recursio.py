# Example of the factorial of any number  by the help of recursion

def fact(num):
    if num==1 or num==0:
        return 1
    else:
        return num*fact(num-1)


num=int(input("Enter the number : "))
fac=fact(num)
print(fac)