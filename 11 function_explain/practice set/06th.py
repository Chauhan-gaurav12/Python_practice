# write a python function that convert inches to cms
# formula of convert 1 inch to cm is (1*2.54)
# 1 cm to inch is (1*0.394)

def converter(inch):
    a=inch*2.54
    print(f"{inch} inch is {a} cm ")

inch=int(input("Enter the inch value : "))
converter(inch)