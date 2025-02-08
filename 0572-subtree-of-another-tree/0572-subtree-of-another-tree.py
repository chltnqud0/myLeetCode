# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = [root]

        while stack:
            temp = stack.pop()

            if self.comparison(temp, subRoot):
                return True
            
            if temp.left:
                stack.append(temp.left)
            if temp.right:
                stack.append(temp.right)


        return False


    def comparison(self, a, b):
        if a.val != b.val:
            return False
        
        if bool(a.left)^bool(b.left):
            return False
        
        if bool(a.right)^bool(b.right):
            return False

        if a.left and b.left and a.right and b.right:
            return self.comparison(a.left, b.left) and self.comparison(a.right, b.right)

        elif a.left and b.left:
            return self.comparison(a.left, b.left)

        elif a.right and b.right:
            return self.comparison(a.right, b.right)

        return True