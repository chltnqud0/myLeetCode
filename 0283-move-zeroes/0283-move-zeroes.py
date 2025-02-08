class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums
        count = 0
        if nums[0] == 0:
            count += 1
        for i in range(1, len(nums)):
            if nums[i] == 0:
                count += 1
            else:
                nums[i- count], nums[i] = nums[i], nums[i - count]

        return nums