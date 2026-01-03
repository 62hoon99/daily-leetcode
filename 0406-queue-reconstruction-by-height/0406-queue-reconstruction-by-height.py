class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # 1. 키 내림차순, k 오름차순 정렬
        people.sort(key=lambda x: (-x[0], x[1]))

        answer = []

        # 2. k 위치에 바로 삽입
        for height, k in people:
            answer.insert(k, [height, k])

        return answer