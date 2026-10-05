class Solution(object):
    def findErrorNums(self, nums):
        n=len(nums)
        expected=n*(n+1)//2
        exact=sum(nums)
        result=[]
        nums.sort()
        for i in range(n-1):
            if nums[i]==nums[i+1]:
                repeat=nums[i]
                result.append(repeat)

        missing=expected-exact +repeat
        result.append(missing)
        return result
