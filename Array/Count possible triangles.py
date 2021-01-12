class Solution:
    def findNumberOfTriangles(ob, arr, n):
        #code here
        a=n
        facto_n=1
        while a>0:
            facto_n*=a
            a-=1
        b=n-3
        facto_n_=1
        while b>0:
            facto_n_*=b
            b-=1
        return int(facto_n/(6*facto_n_))
