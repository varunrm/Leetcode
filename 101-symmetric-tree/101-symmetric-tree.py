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
        self.isvalid=True
        self.daafs(root.left,root.right)
        return self.isvalid
        
    def daafs(self,left,right):
        if left== None and right== None:
            return
        if left==None or right==None or right.val!=left.val:
            self.isvalid=False
            return   
        if self.isvalid:
            self.daafs(left.left,right.right)
            self.daafs(left.right,right.left)