# Write a program using function to convert celsuis to fahrenheit 
# formula of convert 1 celsuis  (1*9/5)+32
# formula to convert 1 fahrenhit to celsuis is ((1-32)*5/9)
def convert(cels):
    fahre=(cels*9/5)+32
    print(f"The fahrenheit of {5} celsuis is  {fahre}")

a=int(input("Enter the value in  celsuis : "))
convert(a)