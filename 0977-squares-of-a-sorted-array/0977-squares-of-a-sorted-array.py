class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums.sort(key=abs)
        return [x**2 for x in nums]