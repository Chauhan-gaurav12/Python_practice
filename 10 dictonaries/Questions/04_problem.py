# If the name sof two friends are same what will happen to the programm in the problem 3 
# answer--- so the last giving language is print on that name and key can't be duplicate
d={}
name=input("Enter Friends name : ")
lang=input("Enter Language name: ")
d.update({name:lang})
name=input("Enter Friends name : ")
lang=input("Enter Language name: ")
d.update({name:lang})
name=input("Enter Friends name : ")
lang=input("Enter Language name: ")
d.update({name:lang})


print(d)

# But if we give two language name is and key is diffrent so that  will print because vakue can be duble in a dict
