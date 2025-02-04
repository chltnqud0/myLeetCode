class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]
        answer = [0, 1]
        temp = 1
        now = 1
        for i in range(2, n + 1):
            if now == temp:
                answer.append(1)
                temp *= 2
                now = 1
            else:
                answer.append(answer[now] + 1)
                now += 1
        return answer