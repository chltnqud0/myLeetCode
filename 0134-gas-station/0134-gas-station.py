class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        l = []
        length = len(gas)
        for i in range(length):
            l.append(gas[i] - cost[i])

        if sum(l) < 0:
            return -1

        summary = 0
        point = 0

        for i in range(length):
            summary += l[i]

            if summary < 0:
                summary = 0
                point = i + 1
            
        return point