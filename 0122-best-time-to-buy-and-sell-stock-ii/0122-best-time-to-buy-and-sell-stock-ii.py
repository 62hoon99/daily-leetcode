class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pre = 10001
        answer = 0

        for p in prices:
            if pre > p:
                pre = p
                continue
            
            answer += p - pre
            pre = p
        
        return answer
