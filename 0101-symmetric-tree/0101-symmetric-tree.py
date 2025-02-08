# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return True
        
        if bool(root.left)^bool(root.right):
            return False

        dq = deque([root.left, root.right])
        # print(dq)
        # print(dq.popleft())
        # print(dq.pop())
        while dq:
            a, b = dq.popleft(), dq.pop()

            # print(a)
            if a.val != b.val:
                return False
            
            if bool(a.left)^bool(b.right):
                return False
            elif a.left and b.right:
                dq.appendleft(a.left)
                dq.append((b.right))
            
            if bool(a.right)^bool(b.left):
                return False
            elif a.right and b.left:
                dq.appendleft(a.right)
                dq.append(b.left)
        
        return True