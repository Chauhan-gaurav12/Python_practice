f=open("gaura.txt")
# line1=f.readline() # If we want to read only a single line 
# print(line1,type(line1))
# line2=f.readline() # It will print second line
# print(line2,type(line2))
# line3=f.readline() # It will print third line  
# print(line3,type(line3))
# line4=f.readline() # It will print fourth line 
# print(line4,type(line4))
# f.close()

# s=open("gaura.txt")
# lines=s.readlines() # It will all lines at a same time
# print(lines)
# s.close()


# By using while loop
line=f.readline()
while(line !=""):
    print(line)
    line=f.readline()

f.close() 