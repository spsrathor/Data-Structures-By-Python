for x in range(int(input())):
    n,d = list(map(int, input().split()))
    a = list(map(int, input().split()))
    l=a[d:]
    l.extend(a[:d])
    print(*l)
