
# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def minSubtree(self, root):
        if root is None:
            return [None, 99999999999999999999, 0]
        
        left = self.minSubtree(root.left)
        right = self.minSubtree(root.right)

        node = [root, left[2] + right[2] + root.val, left[2] + right[2] + root.val]

        if left[1] <= node[1]:
            node[1] = left[1]
            node[0] = left[0]
        
        if right[1] <= node[1]:
            node[1] = right[1]
            node[0] = right[0]

        return node

if __name__ == "__main__":
    root = TreeNode(1)
    sol = Solution()
    res = sol.minSubtree(root)
    print(res)
        
