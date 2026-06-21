# we have a problem like we have to sum of the list that list every element is string
li=["45","21","12"]
# l1=[]
# for i in li:
#     i=int(i)
#     l1.append(i)
# print(l1)
# sum=0
# for i in l1:
#     sum+=i
# print("The sum of list is : ",sum)


# we can solve it by map 

def int_converter(a):
    return int(a)

print(sum(map(int_converter,li)))  # we wll get sum 78 

# we have one more method 

print(sum(map(lambda a :int(a) ,li)))  # we write this code in single line