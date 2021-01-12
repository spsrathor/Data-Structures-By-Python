def leaders(A,N):
    #Your code here
    l=[A[-1]]
    m = A[-1]
    for i in range(N-2,-1,-1):
        if m<=A[i]:
            m=A[i]
            l.append(m)
    return l[::-1]
