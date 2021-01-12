class Solution:
    def armstrongNumber(ob, n):
        # code here 
        s=[int(i) for i in str(n)]
        i=0
        for x in s:
           i+=x**3
        if i==n:
            return 'Yes'
        else:
            return 'No'
