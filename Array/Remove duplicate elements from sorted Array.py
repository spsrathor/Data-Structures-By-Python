class Solution:	
	def remove_duplicate(self, A, N):
		# code here
		A=list(set(A))
		A.sort()
		return len(A)
