class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = []

        pre_n1 = -1001
        for i in range(len(numbers)):
            n1 = numbers[i]

            if pre_n1 == n1:
                continue
            for j in range(i+1,len(numbers)):
                n2 = numbers[j]

                if n1 + n2 > target:
                    break
                elif n1 + n2 < target:
                    continue
                else:
                    result.append(i+1)
                    result.append(j+1)
                    return result
            pre_n1 = n1
        
        return result