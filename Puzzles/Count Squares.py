class Solution:
    def countSquares(self, N):
        # code here
        c=1
        count = 0
        n = N**(1/2)
        if n == int(n):
            return int(n-1)
        else:
            return int(n)
