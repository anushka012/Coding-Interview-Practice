# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def rec(p, q):
            if (p and (not q)) or ((not p) and q):
                return False
            if (not p) and (not q):
                return True
            if p.val != q.val:
                return False
            return rec(p.left, q.left) and rec(p.right, q.right)
        return rec(p, q)