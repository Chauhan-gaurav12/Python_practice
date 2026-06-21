# write a python function to print the multiplication table of the given number
def mul(num):
    for i in range(1,11):
        product=num*i
        print(f"{num} * {i} = {product}")

num=int(input("Enter the number : "))
mul(num)