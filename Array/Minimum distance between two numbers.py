def minDist(arr, n, x, y):
    # Code here
    r=-1
    if (x in arr) and (y in arr):
        xl = []
        diff = []
        for i in range(len(arr)):
            if x==arr[i]:
                xl.append(i)
        for i in range(len(arr)):
            if y==arr[i]:
                temp = xl
                temp = [abs(i-yi) for yi in temp]
                diff.extend(temp)
        r=min(diff)
    return r
