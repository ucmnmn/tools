'''
Created on Apr 12, 2018

@author: Administrator
'''
'find the balance number of list'


a=[1,3,5,7,9]

sum1=0
balance=0
for i in a:
    sum1=sum1+int(i)
for j in range(0,len(a)):
    balance=balance+a[j]
    if balance==(sum1-a[j+1])/2:
        print(a[j+1])
        break
    else:
        print("next")
        continue