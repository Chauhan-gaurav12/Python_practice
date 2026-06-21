# name=input("Enter the name : ").lower() # we can use a method in input time it is also possible 

# print(name)

# print("Hi ,",name.capitalize())
# print("Hi ,",name.lower())
# g="""My name is gaurav rajput 
#     i am from dhampur 
#         but i resides at Nainsi wala in dhampu
#             i have done Bca from disha institute of science of technology that is afflicated from MJPRU University bariely"""
# print(g.title())

# .Title() is make the 1st character  capital of every word


# find any word in the string
# String="he is a good boy.he is very happy.he is smarter than you"
# index=String.find("he")
# print(String.find("he",index+1))

# g=String.count("he")
# print(g)
st="gaurav"
up=st.upper() 
#1. This method converts all characters in a string to uppercase.
print(up)

# 2. changig the case of the word

txt="hello world"
print(txt.upper())    # HELLO WORLD
print(txt.lower())    # hello world
print(txt.title())    # Hello World
print(txt.capitalize())  # Hello world
print(txt.swapcase())    # HELLO WORLD → hello world


# 3.  removing the Space 
txt = "   hello   "
print(txt.strip())   # "hello" (removes both ends)
print(txt.lstrip())  # "hello   " (removes left spaces)
print(txt.rstrip())  # "   hello" (removes right spaces)

#  4. Finding and searching

txt = "python programming"
print(txt.find("pro"))   # 7 (index where found)
print(txt.rfind("o"))    # 14 (last index of 'o')
print(txt.index("pro"))  # 7 (like find but gives error if not found)
print(txt.count("o"))    # 3 (number of times 'o' appears) 

# 5. replacing & modifying 

txt = "I love Java"
print(txt.replace("Java", "Python"))  # I love Python

# 6. Formatting Strings

txt = "I like {0} and {1}"
print(txt.format("Python", "Java"))  # I like Python and Java

name = "Shanu"
age = 21
print(f"My name is {name}, I am {age}")  # f-string method

# 7. Checking content 

txt = "Python3"
print(txt.isalpha())   # False (contains numbers)
print("Python".isalpha())  # True (only letters)
print(txt.isdigit())   # False
print("123".isdigit()) # True
print(txt.isalnum())   # True (letters + numbers)
print("   ".isspace()) # True (only spaces)
print("python".islower())  # True
print("PYTHON".isupper())  # True
print("Python Programming".istitle())  # True


# 8. Splitting & Joining
txt = "apple,banana,cherry"
print(txt.split(","))   # ['apple', 'banana', 'cherry']

words = ["I", "love", "Python"]
print(" ".join(words))  # I love Python

# 9. Allignment 

txt = "Python"
print(txt.center(20, "-"))  # -------Python-------
print(txt.ljust(20, "*"))   # Python**************
print(txt.rjust(20, "*"))   # **************Python

# 10. Checking Start & End 

txt = "Python programming"
print(txt.startswith("Python"))  # True
print(txt.endswith("ing"))       # True

