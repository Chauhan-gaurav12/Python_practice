# Main thing to notice is that every null is give false like as {},[],(),"",0 will return false

if {}:
    print("true")
else:
    print("False")



if[]:
        print("true")
else:
    print("False")

    # in this if we will provide aby value so it will return true

if[1,2]:
         print("true")
else:
    print("False")

print(type([1,2]))
a=(1,2)
b={1,2}
c={"Gaurav","vivek"}

print(type(a))
print(type(b))
print(type(c))
