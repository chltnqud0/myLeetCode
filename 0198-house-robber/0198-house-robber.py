class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        elif len(nums) == 2:
            return max(nums)
        
        elif len(nums) == 3:
            return max(nums[0] + nums[2], nums[1])

        else:
            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            dp[2] = max(nums[0] + nums[2], nums[1])

            for i in range(3, len(nums)):
                dp[i] = max(dp[i-3] + nums[i], dp[i-2] + nums[i], dp[i-1])
            
            return max(dp)
            