# 1. create a nested tuple and access element using indexing
# 2. Create a tuple of numbers and print only the even number 
# 3. Write a program to reverse a tuple
# 4. check if two tuple has a common number 
# 5.Create two tuple and concatenate them into a list 
# 6. Write a program to find the index of an element in a tuple 
# 7. write a program to sort the tuple numbers 
# 8. Create a tuple of Strings and find the longest String

# 1st answer 

# tup=((10,20,30),(40,50,60),(70,80,90))
# # access the 30 from the tuple
# print(tup[0][2])

# # access 80
# print(tup[2][1]) 


# 2nd answer

# tup1=(14,25,1,36,77,25,62,98,78,65)
# for i in tup1:
#     if i%2==0:
#         print(i)

# 3rd answer

# tup1=(25,47,87,98,45,10)
# reversed_tup=tup1[::-1]
# print(reversed_tup)

# answer 4 
"""tup2=(5,54,323)
common=set(tup).intersection(tup2)
print("The common element is ",common)

"""


# 5th  Answer 

tup=(78,54,65,87,98,52,10,21,32,33)
# tup1=(7887,7412)
# result=tup+tup1
# my_list=list(result)
# print(my_list)

# 6th answer
# tup4=(10,20,30,40,50,60,70,80,90,100)
# index=tup4.index(20)
# print(index)

# 7th answer
# sorted=tuple(sorted(tup))
# print(sorted)

# 8th answer

# words=("Mango","Gaurav is a good boy","he is a very smart and clever boy")
# longest=max(words,key=len)
# print(longest)
