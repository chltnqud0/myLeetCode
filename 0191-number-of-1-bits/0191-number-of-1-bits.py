class Solution:
    def hammingWeight(self, n: int) -> int:
        answer = 0
        a = 1
        while n != 0:
            if n == a:
                return answer + 1
            if n > a:
                a *= 2
                continue
            else:
                n -= a // 2
                a = 1
                answer += 1
        return answer