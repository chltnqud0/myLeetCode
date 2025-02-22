class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        for i in range(len(nums)-1,0,-1):
            if nums[i] > nums[i-1]:
                f = [ (a,b) for a,b, in enumerate(nums) if b > nums[i-1] and a > i -1]
                index = min(f, key= lambda x: (x[1] - nums[i-1], -x[0]))
                print(index)
                temp = nums.pop(index[0])
                print(temp)
                nums[i-1:] = sorted(nums[i-1:])
                nums.insert(i-1, temp)
                break
        else:
            nums.sort()