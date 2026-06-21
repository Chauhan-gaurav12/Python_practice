#check igiven list is str or not
l1=["Garav",15,"Vivek"]
list2=[]
for i in l1:
    list2.append(isinstance(i,str))
print(list2)

print(isinstance(15,int)) # it is use to check the type 