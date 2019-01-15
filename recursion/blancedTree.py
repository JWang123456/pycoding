
# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def isBalanced(self, root):
        return self.maxDepth(root) != -1

    def maxDepth(self, root):
        if root is None:
            return 0
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        
        return max(left, right) + 1