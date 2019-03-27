def getindex(string,substr):
    l=[];x=0
    str1=string
    c=str1.count(substr)
    for i in range(0,c):
        a=str1.index(substr)
        y=a
        a+=x
        str1=str1[y+1::]
        x=a+1
        l.append(a)
    return l
