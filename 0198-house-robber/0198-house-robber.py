class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        memory = [0] * len(nums)
        memory[0] = nums[0]
        memory[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            memory[i] = max(memory[i-2] + nums[i], memory[i-1])
        
        return memory[-1]