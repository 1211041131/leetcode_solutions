class Solution(object):
    def searchInsert(self, nums, target):
        n = len(nums)
        ub = n
        low = 0
        high = n - 1

        while low<=high:
            mid=(low+high)//2
            if nums[mid]>=target:
                high=mid -1
                ub=mid
            else:
                low=mid+1
        return ub
            

            