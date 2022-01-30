# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        x = self.isBalanced_helper(root)
        if x!= -1:
            return True
        return False
    
    def isBalanced_helper(self, root):
        if root == None:
            return 0
        lh = self.isBalanced_helper(root.left)
        if lh == -1:
            return -1
        rh = self.isBalanced_helper(root.right)
        if rh == -1:
            return -1
        if abs(lh-rh)>1:
            return -1
        return 1+max(lh,rh)
        