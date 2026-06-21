# Check that a given element is exists in a tuple or not
tup=(25,1,2,3,4,5,6,7,7,556.3556,5,5)
a=int(input("Enter what you want to search: "))
if a in tup:
    print("It is exist")
else:
    print("not exist")