# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return
        answer = TreeNode(nums[len(nums) // 2])
        answer.left = self.sortedArrayToBST(nums[: len(nums) // 2])
        if len(nums) == 2:
            return answer
        else:
            answer.right = self.sortedArrayToBST(nums[len(nums) // 2 + 1 :])

        return answer