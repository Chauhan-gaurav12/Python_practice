# for this problem file name is file.txt

# problem is - A file contain a word donkey multiple time .we need to write a program which replce this word 
# -- with ###### by updating the same file

word="donkey"
with open(f"file.txt","r") as f:
    content=f.read()

content_new=content.replace("donkey","######")
with open("file.txt",'w') as f:
    f.write(content_new)