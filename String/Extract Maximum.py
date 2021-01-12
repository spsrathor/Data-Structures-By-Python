import re
class Solution:
    def extractMaximum(self,S): 
        # code here
        r = list(map(int, re.findall('\d+',S)))
        if r==[]:
            return -1
        else:
            return max(r)
