
# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxDepth(self, root):
        # write your code here
        if root is None:
            return 0
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        
        res = max(left, right) + 1
        
        return res

# Driver code
root = TreeNode(1)
node = TreeNode(3)
rnode = TreeNode(8)
root.left = node
node.right = rnode

obj = Solution()
t = obj.maxDepth(root)

print(t)