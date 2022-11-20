# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def dfs(root,m):
            if root==None :
                return
            if root.val>=m:
                self.count+=1
            dfs(root.left,max(m,root.val))
            dfs(root.right,max(m,root.val))
                
        m=float('-inf')
        self.count=0
        dfs(root,max(m,root.val))
        return self.count
                
            