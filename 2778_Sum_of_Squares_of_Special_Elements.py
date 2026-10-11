class Solution(object):
    def sumOfSquares(self, nums):
        n=len(nums)
        total=0
        k=0
        for i in range(n):
            if n % (i+1)==0:
                total=total+nums[i]*nums[i]
                k+=1
            
        return total 
