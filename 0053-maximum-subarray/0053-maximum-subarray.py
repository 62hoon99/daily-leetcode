class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0
        result = -10001
        for n in nums:
            sum += n
            result = max(result, sum)
            if sum < 0:
                sum = 0
        return result