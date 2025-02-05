class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = ''
        shortest_length = min(len(s) for s in strs)
        temp = ''
        for i in range(shortest_length):
            for j in range(len(strs)):
                if j == 0:
                    temp = strs[j][i]
                else:
                    if strs[j][i] != temp:
                        return answer
            else:
                answer += temp
        return answer