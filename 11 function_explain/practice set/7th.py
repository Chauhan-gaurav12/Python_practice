# Write a python function to remove a given word from a list strip at the same time 

def rem(l,word):
    n=[]
    for i in l:
        if not (i==word):
            n.append(i.strip(word))
    return n





l=["gaurav","Rohan","suman","an"]
word=input("Enter the word that you want to strip: ")
print(rem(l,word))
