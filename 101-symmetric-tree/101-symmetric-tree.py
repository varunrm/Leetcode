# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root==None:
            return True
        return self.daafs(root.left,root.right)
        
        
    def daafs(self,left,right):
        if left== None and right== None:
            return True
        if left==None or right==None or right.val!=left.val:
            return False  
        return self.daafs(left.left,right.right) and self.daafs(left.right,right.left)