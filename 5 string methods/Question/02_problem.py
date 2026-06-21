# write a program to to fill in a letter templete   given below with the name and date 
"""
    Dear |Name|,
    You are selected !
    |Date|
"""

name=input("Enter the name : ")
# date=int(input("Enter the date : "))

letter='''
            Dear |Name|,
            You are selected !
            |Date|
'''
print(letter.replace("|Name|" ,name).replace("|Date|","26 sep 2025"))
