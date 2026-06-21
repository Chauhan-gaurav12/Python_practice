a={"name":"Gaurav" ,
   "city": "noida",
   "marks": 85   
   }
b={
    "subject": "PCM"
}

#  a.clear() # used to empty the dict
# copym=b.copy()
# print(copym)

#  print(a.get("name")) # for getting the element from the doctionaries
# print(a.pop("marks"))
# print(a)

# print(a.update("Name"  "Kartik"))
# print(a)

print(a.items()) # by using this we get dictionary in the form of tuple so we can itrate it easily

print(a.keys()) # it will tell us howmany keys is exist in the dictionary
# if we want ot find the vlaue in the list only so 
print(a.values())
a.update({"marks": 99,"address":"Dhampur"}) # in this if we give name of any one and that is not exist in the dict so that will add in the list
print(a["marks"])
print(a)

print(a.get("marks"))

