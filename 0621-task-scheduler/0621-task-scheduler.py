class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        counter = Counter(tasks)

        # 실행 가능한 task들
        available = []

        # (다시 사용 가능해지는 시간, task)
        cooldown = deque()

        for task, cnt in counter.items():
            available.append(task)

        while available or cooldown:
            time += 1

            # 1️. 쿨타임 끝난 task 복귀
            if cooldown and cooldown[0][0] == time:
                _, task = cooldown.popleft()
                available.append(task)

            # 2. 실행 가능한 task 중 greedy 선택
            if available:
                # 가장 많이 남은 작업
                task = max(available, key=lambda x: counter[x])
                available.remove(task)

                counter[task] -= 1
                if counter[task] > 0:
                    cooldown.append((time + n + 1, task))
            # else: idle (time만 증가)

        return time