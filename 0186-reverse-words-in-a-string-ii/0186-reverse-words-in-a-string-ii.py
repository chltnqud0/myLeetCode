class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = 0

        for i in range(len(s)):
            if s[i] == ' ':
                right = i - 1
                for j in range((right - left + 1) // 2):
                    s[left + j], s[right - j] = s[right - j], s[left + j]
                left = i + 1
        else:
            right = len(s) - 1
            for j in range((right - left + 1) // 2):
                s[left + j], s[right - j] = s[right - j], s[left + j]
        s.reverse()        