for x in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    num = int(input())
    count = 0
    arr.sort()
    for x in arr:
        if x<=num:
            count+=1
        else:
            break
    print(count)
