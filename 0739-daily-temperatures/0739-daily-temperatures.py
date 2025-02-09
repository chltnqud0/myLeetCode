import heapq
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        hq = []
        heapq.heappush(hq, [temperatures[0], 0])
        
        for i, t in enumerate(temperatures[1:],start=1):
            while hq and hq[0][0] < t:
                a = heapq.heappop(hq)[1]
                answer[a] = i - a
            heapq.heappush(hq, [t, i])

        return answer