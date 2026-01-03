class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        count = Counter()
        answer = 1

        while right < len(s):
            count[s[right]] += 1
            most = count.most_common()[0][1]

            if right + 1 -left -most <= k:
                answer = max(answer, right + 1 -left)
            else:
                count[s[left]] -= 1
                left += 1
            right += 1
        
        return answer