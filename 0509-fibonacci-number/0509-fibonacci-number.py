class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        
        dp = [0] * (n + 1)
        dp[1] = 1

        def recur(num):
            if num <= 0:
                return 0
            if dp[num] > 0:
                return dp[num]
            
            dp[num] = recur(num-1) + recur(num-2)
            return dp[num]
        
        return recur(n)
