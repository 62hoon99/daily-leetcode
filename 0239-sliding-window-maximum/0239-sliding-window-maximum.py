class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = []
        memory = defaultdict(int)

        left = 0
        right = 0
        result = []

        while right <= len(nums):
            if right < k:
                heapq.heappush(q, -nums[right])
                right += 1
                continue
            elif right < k and right == len(nums):
                break
            
            while memory[-q[0]] > 0:
                memory[-q[0]] -= 1
                heapq.heappop(q)
            
            result.append(-q[0])

            memory[nums[left]] += 1
            left += 1

            if right < len(nums):
                heapq.heappush(q, -nums[right])
            right += 1

        if len(result) == 0:
            result.append(heapq.heappop(q))
        
        return result