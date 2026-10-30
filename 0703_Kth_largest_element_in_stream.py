import heapq
class KthLargest(object):

    def __init__(self, k, nums):
        self.k=k
        nums.sort()
        self.pq=[]
        for i in range(min(len(nums),k)):
            heapq.heappush(self.pq,nums[i])
        for i in range(k,len(nums)):
            if nums[i]>self.pq[0]:
                heapq.heappop(self.pq)
                heapq.heappush(self.pq,nums[i])
    def add(self, val):
        if len(self.pq) < self.k:
            heapq.heappush(self.pq, val)
        elif val>self.pq[0]:
            heapq.heappop(self.pq)
            heapq.heappush(self.pq,val)
        return self.pq[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)