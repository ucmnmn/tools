import random


for count in range(5):
    id_prefix = '6245647845412'  # define the card id,15 digit number
    id_suffix = random.randint(10000, 99999)  # random number for 16-18
    bankid = id_prefix + str(id_suffix)  # connect the prefix and suffix

    sum = 0  # the count var
    for i in range(len(bankid) - 1, 0, -2):  # from last one to first one,the sum of odd position number
        sum += int(bankid[i])    
    for j in range(len(bankid) - 2, 0, -2):  # from last one to first one 
        if int(bankid[j]) * 2 > 10:  # the even position number multiply by 2,and if more than 10,then minus 9
            sum += int(bankid[j]) - 9
        else:
            sum += int(bankid[j])          
    thelast = sum % 10   
    if thelast > 0:  # check the last number,make sum%10 is 0,if not ,plus the result of 10-sum%10
        bankid = bankid + str(10 - thelast)
    else:
        bankid = bankid + '0'
    print(bankid)

