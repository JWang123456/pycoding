# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def flatten(self, root):
        self.helper(root)

    def helper(self, root):

        if root == None:
            return None

        leftlastnode = self.helper(root.left)
        rightlastnode = self.helper(root.right)

        if leftlastnode != None:
            leftlastnode.right = root.right
            root.right = root.left
            root.left = None

        if rightlastnode != None:
            return rightlastnode
        if leftlastnode != None:
            return leftlastnode
        
        return root