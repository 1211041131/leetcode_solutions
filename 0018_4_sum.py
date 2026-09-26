class Solution(object):
    def fourSum(self, nums, target):
        n = len(nums)
        nums.sort()
        result = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                seen = {}
                curr_sum = nums[i] + nums[j]
                for k in range(j + 1, n):
                    missing = target - (nums[k] + curr_sum)
                    if missing in seen:
                        quad = [
                            nums[seen[missing]],
                            nums[i],
                            nums[j],
                            nums[k]
                        ]
                        quad.sort()
                        if quad not in result:
                            result.append(quad)
                    seen[nums[k]] = k
        return result