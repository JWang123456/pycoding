# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the maximum average of subtree
    """
    # best node and avg
    result = [None, 0]
    
    def findSubtree2(self, root):
        self.helper(root)
        return self.result[0]

    def helper(self, root):
        if root is None:
            return [0, 0]
        
        left = self.helper(root.left)
        right = self.helper(root.right)

        sum = root.val + left[0] + right[0]
        size = 1 + left[1] + right[1]
        avg = sum/size
        
        if self.result == [None, 0] or self.result[1] < avg:
            self.result = [root, avg]
        
        res = [sum, size]

        return res


        