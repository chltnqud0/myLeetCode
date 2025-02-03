class Solution:
    def romanToInt(self, s: str) -> int:
        answer = 0

        before = ''
        for i in s:
            if i == 'I':
                answer += 1
                
            elif i == 'V':
                if before == 'I':
                    answer += 3
                else:
                    answer += 5
                
            elif i == 'X':
                if before == 'I':
                    answer += 8
                else:
                    answer += 10
                
            elif i == 'L':
                if before == 'X':
                    answer += 30
                else:
                    answer += 50
                
            elif i == 'C':
                if before == 'X':
                    answer += 80
                else:
                    answer += 100
                
            elif i == 'D':
                if before == 'C':
                    answer += 300
                else:
                    answer += 500
                
            else:
                if before == 'C':
                    answer += 800
                else:
                    answer += 1000
            before = i
        return answer