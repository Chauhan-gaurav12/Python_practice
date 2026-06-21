# we can give a default value when we are calling a function

def greet(name, ending="Thank you"): # In ending we are giving a default alue if we are not giving any value so thanku you will assign to ending 

    print(f"Good day ,{name}")
    print(ending)
name=input("Enter the name : ")
greet(name,"Thanks")