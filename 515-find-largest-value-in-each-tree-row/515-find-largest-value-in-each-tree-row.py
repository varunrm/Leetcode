# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        if root is None: 
            return
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.maxi=[]
        self.helper(root,level=0)
        return self.maxi
    def helper(self,root,level):
        if root is None: 
            return
        if len(self.maxi)<level+1:
            self.maxi.append(root.val)
        self.maxi[level]=max(self.maxi[level],root.val)
        self.helper(root.left,level+1)
        self.helper(root.right,level+1)
    