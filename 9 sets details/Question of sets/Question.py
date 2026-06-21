# 1. write a program to find the maximum and minimum element in a numeric set
# 2. write a program to check that two sets are disjoint
# 3. convert a list to a set and set to list
# 4. give two set check whether they at least one element in common fint that 
# 5. write a program to count the number of unique element in a list using set
# 6. remove a element from the set without using remove method
# 7. create a set of string and check whether a particular string is exists in it


# #1 answer
 
# set1={12,34,45,56,87,1111}
# print("Maximum number is : ",max(set1))
# print("Maximum number is : ",min(set1))

# #2nd answer
# set2={12,1,12,34}
# set3={112,30}
# print("set2 and set3 is disjoint: ",set2.isdisjoint(set3)) # disjoint meaning is diffrence 


# #3rd answer


# list1=[12,"Gaurav","salar",21,87,21,21,21]
# set4=set(list1)
# print("converted set is : ",set4) # it is changing list to set 
# again_list=list(set4)
# print("Converted list is : ",list(set4))
# print(type(again_list))

# 4th answer
set5={12,123,34,54,65}
set6={12,"Gaurav"}
print(set5.intersection(set6))

# 5th answer
list2=[12,12,12,32,43,23,43,3,4,5,3,4,0,988]
set7=set(list2)
print("The unique element in the list is : ",len(set7))

#6th  set
set1={65,45,56,65,25,52,41,14}
print("Before removing set is : ",set1)
set1.pop()
print("after removing set is : ",set1)

# 7th question answer

fruits={"Mango","orange","banana"}

print("grapes in sets : ","grapes" in fruits) # in is use to sarch anything in the list
