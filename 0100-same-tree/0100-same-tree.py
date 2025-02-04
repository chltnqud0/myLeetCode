# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not all([p, q]):
            return False
        stack = [[p, q]]
        while stack:
            a, b = stack.pop()
            if a.val != b.val:
                return False
            if bool(a.left)^bool(b.left):
                return False
            if bool(a.right)^bool(b.right):
                return False
            
            if a.left:
                stack.append([a.left, b.left])
            if a. right:
                stack.append([a.right, b.right])
        
        return True