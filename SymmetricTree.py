# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traversal1(self, root):
        if not root:
            self.result1.append(None)
        else:
            self.result1.append(root.val)
            
            self.traversal1(root.left)
            self.traversal1(root.right)
                
    def traversal2(self, root):
        if not root:
            self.result2.append(None)
        else:
            self.result2.append(root.val)
            
            self.traversal2(root.right)
            self.traversal2(root.left)
                
                
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root:
            if not root.left and not root.right:
                return True
            if root.left and root.right:
                self.result1, self.result2 = [], []
                self.traversal1(root.left)
                self.traversal2(root.right)
                
                if self.result1 == self.result2:
                    return True
                else:
                    return False
            else:
                return False