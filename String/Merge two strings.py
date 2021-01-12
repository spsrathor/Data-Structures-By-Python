for x in range(int(input())):
    s1,s2 = list(input().split(' '))
    l=[list(s1),list(s2)]
    m = min(len(l[0]),len(l[1]))
    lm = l[0]
    if m==len(l[0]):
        lm=l[1]
    l1=[]
    for i in range(m):
        l1.append(l[0][i])
        l1.append(l[1][i])
    l1.extend(lm[i+1:])
    print(*l1,sep='')
