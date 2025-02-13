class Solution:
    def calculate(self, s: str) -> int:
        s1 = []
        s2 = []
        flag = -1
        answer = 0
        temp = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] == ' ':
                flag = -1
                continue
            elif s[i] == ')':
                flag = -1
                if s1:
                    s2.append(s1)
                    s1 = [0]
                else:
                    s1.append(0)
                pass
            elif s[i] == '(':
                flag = -1
                temp += sum(s1)
                if s2:
                    s1 = s2.pop()
                else:
                    s1 = []
                pass
            elif s[i] == '+':
                flag = -1
                if s1:
                    s1.append(temp)
                else:
                    answer += temp
                temp = 0
                pass
            elif s[i] == '-':
                flag = -1
                if s1:
                    s1.append(-temp)
                else:
                    answer -= temp
                temp = 0
                pass
            else:
                flag += 1
                if flag != -1:
                    temp = int(s[i]) * (10 ** flag)  + temp
                else:
                    temp = int(s[i])
        
        answer += temp
        return answer