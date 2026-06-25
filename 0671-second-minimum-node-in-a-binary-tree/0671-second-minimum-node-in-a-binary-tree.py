# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        vals=[]
        def dfs(node):
            if not node:
                return
            vals.append(node.val)
            dfs(node.left)  
            dfs(node.right)
        dfs(root)
        vals=sorted(set(vals))
        if len(vals)<2:
            return -1
        return vals[1]          
       
        