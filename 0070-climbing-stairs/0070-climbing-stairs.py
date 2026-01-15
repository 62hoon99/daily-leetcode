class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        memory = [0] * (n + 1)
        memory[1] = 1
        memory[2] = 2

        def recursive(step):
            if memory[step] > 0:
                return memory[step]
            
            memory[step] = recursive(step - 1) + recursive(step - 2)
            return memory[step]
        
        recursive(n)

        return memory[n]