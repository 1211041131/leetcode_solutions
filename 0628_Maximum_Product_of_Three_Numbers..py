class Solution(object):
    def maximumProduct(self, nums):
        maxi=float("-inf")
        nums.sort()
        product=nums[-1]*nums[0]*nums[1]
        product2=nums[-1]*nums[-2]*nums[-3]
        maxi=max(product,product2)
        return maxi