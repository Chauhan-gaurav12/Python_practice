# copy,update,clear

set1={54,25,21,14}
set2={25,54,47,54}

# use of copy set 
copyset=set1.copy() # It will copy all element of set1 to copyset
print(copyset)


#Use of update 

set1.update(set2) # It will update set add set2 value in the set1
print(set1)

# use of clear 

a=set2.clear()
print(a)
print(type(a))
