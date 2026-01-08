class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        
        farthness = 0
        end = 0
        count = 0

        for i in range(n - 1):
            if farthness < i + nums[i]:
                farthness = i + nums[i]
            
            if i == end:
                end = farthness
                count += 1
        
        return count