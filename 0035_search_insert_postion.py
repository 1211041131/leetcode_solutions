class Solution(object):
    def searchInsert(self, nums, target):
        n = len(nums)
        ub = n
        low = 0
        high = n - 1
        

        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                return mid
            else:
                if nums[mid]>target:
                    high=mid-1
                else:
                    low=mid+1
        return lows