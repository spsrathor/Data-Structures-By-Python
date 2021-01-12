def printPat(n):
    #Code here
    #n=2
    y=n
    s=''
    while y>0:
        for i in range(0,n):
            for x in range(0,y):
                s+='{} '.format(n-i)
        s+='$'
        y-=1
    return s
