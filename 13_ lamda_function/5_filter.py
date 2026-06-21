l1=["Gaurav",45,"vivek",15]
print(list(map(lambda x :isinstance(x,str),l1)))  

#we have seen in this we are etting true and false it is not 
#     returning the str name 


# let we are using filter on the place of map

print(list(filter(lambda x : isinstance(x,str),l1))) # by using this we are getting string name 

print(sum(filter(lambda x :isinstance(x,int),l1)))  # it will return of all integer value present in the list


# filter -- it return only these value that are giving true 