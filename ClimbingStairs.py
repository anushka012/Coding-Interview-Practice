class Solution(object):
    	def climbStairs(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		if n==1:
			return 1
		elif n==2:
			return 2
		elif n==3:
			return 3 

		prev_2, prev_1 = 1, 2
		res = 0
		for i in range(3, n+1): 
			res = prev_2 + prev_1
			prev_2 ,prev_1 = prev_1, res
		return res