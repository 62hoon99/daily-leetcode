class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # s 중에서 g[i] 이상인데 제일 작은 거 찾아서 빼면 됨.

        q = []
        for cookie in s:
            heapq.heappush(q, cookie)
        
        g.sort()

        result = 0
        for child in g:
            while len(q) > 0 and q[0] < child:
                heapq.heappop(q)
            
            if len(q) == 0:
                break
            
            heapq.heappop(q)
            result += 1
        
        return result