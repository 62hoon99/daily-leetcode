# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, t1: Optional[TreeNode], t2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not t1 and not t2:
            return None
        
        val = (t1.val if t1 else 0) + (t2.val if t2 else 0)
        node = TreeNode(val)
        
        node.left = self.mergeTrees(t1.left if t1 else None, t2.left if t2 else None)
        node.right = self.mergeTrees(t1.right if t1 else None,t2.right if t2 else None)
        
        return node