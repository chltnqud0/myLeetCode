class Solution:
    def trap(self, height: List[int]) -> int:
        answer = 0

        left_lst = [0] * len(height)
        right_lst = [0] * len(height)

        left = 0
        for i in range(len(height)):
            left = max(left, height[i])
            left_lst[i] = left - height[i]

        right = 0
        for i in range(len(height)-1,-1,-1):
            right = max(right, height[i])
            right_lst[i] = right - height[i]

        for i in range(len(height)):
            answer += min(left_lst[i], right_lst[i])

        return answer
        