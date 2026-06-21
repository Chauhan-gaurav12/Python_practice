# convert a tuple in a list and a list in tuple
tup=(34,23,54,"Gaurav","Chauhan")
list1=list(tup)
print(list1)

tup1=tuple(list1)
print(tup1)
print(type(tup1))
print(type(list(tup)))
