# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    longest: int = 0

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node == None:
                return (None, 0)
            
            left_val, left_max = dfs(node.left)
            right_val, right_max = dfs(node.right)

            result = 0
            node_max = 0
            if left_val == node.val:
                result += (left_max + 1)
                node_max = max(node_max, left_max + 1)
            if right_val == node.val:
                result += (right_max + 1)
                node_max = max(node_max, right_max + 1)
            
            self.longest = max(self.longest, result)

            return (node.val, node_max)
        
        dfs(root)

        return self.longest
            
            
