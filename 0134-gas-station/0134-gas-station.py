class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        load = []
        for i in range(len(gas)):
            load.append(gas[i] - cost[i])
        
        answer = -1
        for i in range(len(load)):
            if load[i] < 0 or (i > 0 and load[i - 1] == load[i]):
                continue
            sum = load[i]
            pos = i + 1

            while pos != i:
                if i == 0 and pos == len(load):
                    break
                if pos == len(load):
                    pos = 0
                sum += load[pos]
                if sum < 0:
                    break
                pos += 1
            
            if sum >= 0:
                return i
        
        return -1

            
        