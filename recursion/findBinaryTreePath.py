
# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def findPath(self, root):
        
        paths = []

        if root is None:
            return paths

        self.helper(root, str(root.val), paths)

        return paths

    def helper(self, root, s, paths):
        if root is None:
            return

        if root.left is None and root.right is None:
            paths.append(s)

        if root.left is not None:
            self.helper(root.left, s + '->' + str(root.left.val), paths)
        
        if root.right is not None:
            self.helper(root.right, s + '->' + str(root.right.val), paths)

        return paths

def Main():
    one = TreeNode(1)
    two = TreeNode(2)
    thr = TreeNode(3)
    fif = TreeNode(5)

    one.left = two
    one.right = thr
    two.right = fif

    sol = Solution()
    res = sol.findPath(one)

    print(res)                                                          

if __name__=='__main__':
    Main()

# class Solution:
#     def findPath(self, root):
        
#         paths = []
#         if root is None:
#             return []

#         l = self.findPath(root.left)
#         r = self.findPath(root.right)

#         for s in l:
#             paths.append(str(root.val) + '->' + s)
        
#         for t in r:
#             paths.append(str(root.val) + '->' + t)

#         if paths == []:
#             paths.append('' + str(root.val))
        
#         return paths
