class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        temp = 0
        answer = -float('inf')
        for n in nums:
            answer = max(answer, n)
            if temp == 0:
                temp = n
            else:
                temp *= n
                answer = max(answer, temp)
        temp = 0
        for i in range(len(nums)-1,-1,-1):
            answer = max(answer, nums[i])
            if temp == 0:
                temp = nums[i]
            else:
                temp *= nums[i]
                answer = max(answer, temp)

        return answer