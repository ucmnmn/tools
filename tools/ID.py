import random

for i in range(10):
    id='37078519761120'+str(random.randint(100,999))
    #the prefix
    num=(7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2)  #the right number list
    sum=0
    for i in range(17):
#     print(id[i],num[i])
        sum+=int(id[i])*int(num[i])
    
    
    last=sum%11
# print("last="+str(last))
    last_num='10X98765432'  #the check number list
# print(last_num[last])
    print(id+last_num[last])