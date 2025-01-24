from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        answer = ""
        target = Counter(t)
        l = len(s)
        for i in range(l):
            if s[i] in target:
                left = i
                right = i
                target[s[i]] -= 1
                break
        else:
            return answer
    
        while True:
            if left == l - 1 and right == l - 1:
                if t == s[left]:
                    answer = t
                break
            if any(v > 0 for v in target.values()):
                if right == l - 1:
                    break
                else:
                    right += 1
                    if s[right] in target:
                        target[s[right]] -= 1
            else:
                if answer == "":
                    answer = s[left: right + 1]
                else:
                    if len(answer) > len(s[left: right + 1]):
                        answer = s[left: right + 1]
                if s[left] in target:
                    target[s[left]] += 1
                left += 1
                

        return answer
