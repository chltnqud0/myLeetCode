# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        answer = ""
        stack = [root]
        while stack:
            temp = stack.pop()
            if not temp:
                answer += " "
                answer += ","
                continue
            answer += str(temp.val)
            answer += ","
            stack.append(temp.left)
            stack.append(temp.right)
        return answer[:-1]

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = data.split(',')
        def myfunc(data):
            
            if data[0] == " ":
                data.pop(0)
                return None
            answer = TreeNode(data[0])
            data.pop(0)
            answer.right = myfunc(data)
            answer.left = myfunc(data)
            return answer

        answer = myfunc(data)
        return answer


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
