class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = []
        if strs == ['']:
            return [['']]
        d = defaultdict(int)
        for s in strs:
            t = ''.join(sorted(s))
            if t in d:
                answer[d[t]].append(s)
            else:
                answer.append([s])
                d[t] = len(answer) - 1
        return answer