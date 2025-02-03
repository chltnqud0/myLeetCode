class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = []
        for i in s:
            if i != '#':
                stack_s.append(i)
            else:
                if stack_s:
                    stack_s.pop()
        
        stack_t = []
        for j in t:
            if j != '#':
                stack_t.append(j)
            else:
                if stack_t:
                    stack_t.pop()
        
        if len(stack_s) != len(stack_t):
            return False
        
        for k in range(len(stack_s)):
            if stack_s[k] != stack_t[k]:
                return False
        
        return True