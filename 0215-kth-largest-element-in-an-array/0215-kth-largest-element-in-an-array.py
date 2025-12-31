class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q = []

        for n in nums:
            heapq.heappush(q, n)
        
        for _ in range(len(nums)-k):
            heapq.heappop(q)
        
        return heapq.heappop(q)