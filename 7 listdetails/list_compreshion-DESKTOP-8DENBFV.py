# we are copying data from a list to another list so we have two method
# first method 

li=[14,89,23,22,12]
b=[]
for i in li:
    if i>40:
        b.append(i)
print(b)

# second method is list comprehension

l3=[i for i in li if i>24] # it add all elements of li  into the  l3
print(l3)