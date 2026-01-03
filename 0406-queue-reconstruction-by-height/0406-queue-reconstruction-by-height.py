class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        q = []
        answer = []

        for p in people:
            heapq.heappush(q, (p[1], p[0]))

        while len(q) > 0:
            count, height = heapq.heappop(q)
            current = 0
            
            for i in range(len(answer) + 1):
                if i == len(answer):
                    answer.append([height, count])
                    break

                if answer[i][0] >= height:
                    current += 1
                
                if current > count:
                    answer.insert(i, [height, count])
                    break
        
        return answer
