def namelist(names):
    value=[]
    print(names)
    for i in names:
        print(i)
        value.append(i['name'])
    value_l=len(value)
    if len(value)<1: return ''
    if len(value)==1: return value[0]
    if len(value)==2: return value[0]+' & '+value[1]
    new=''
    for j in range(len(value)-1):
        new+=value[j]+', '
    new=new[0:-2]+' & '+value[-1]+''
    return new
