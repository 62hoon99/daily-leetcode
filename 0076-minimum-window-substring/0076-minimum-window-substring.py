class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ctr = Counter(t)
        memory = defaultdict(int)

        left = 0
        formed = 0
        required = len(ctr)

        answer = float('inf')
        answer_str = ""

        for right in range(len(s)):
            c = s[right]
            if c in ctr:
                memory[c] += 1
                if memory[c] == ctr[c]:
                    formed += 1

            while formed == required:
                if right - left + 1 < answer:
                    answer = right - left + 1
                    answer_str = s[left:right + 1]

                lc = s[left]
                if lc in ctr:
                    memory[lc] -= 1
                    if memory[lc] < ctr[lc]:
                        formed -= 1
                left += 1

        return answer_str
            
