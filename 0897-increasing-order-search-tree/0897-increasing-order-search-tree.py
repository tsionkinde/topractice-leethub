class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            
            
            self.curr.right = node
            node.left = None
            self.curr = node
            
            inorder(node.right)
        
        dummy = TreeNode(0)
        self.curr = dummy
        
        inorder(root)
        
        return dummy.right