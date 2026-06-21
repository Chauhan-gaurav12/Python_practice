l1=["10","11","12","13","14","89"]
# sum=0
# for i in l1:
#     i=int(i)
#     if i%2==0:
#         sum+=i
# print("The sum is : ",sum)
# print(l1)
# by the help of lambda 
print(sum(list(filter(lambda x:x%2==0,map(int ,l1)))))   # first it is converting and then doing sum of even number 

# l1=["15","14","12","10","89"]
# print(sum(list(filter(lambda x:x%2==0,map(int ,l1)))))  