# rename a file
with open("old.txt") as f:
     content=f.read()

with open("rename_by_python.txt","w") as f:
     f.write(content)

# we have to make a copy of that content and first file we have to dlt but we can't dlt a file we have to use a shutl module
