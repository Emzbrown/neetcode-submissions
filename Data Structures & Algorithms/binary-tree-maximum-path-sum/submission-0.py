# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        count= [root.val]
        def post_order(root):
            if not root:
                return 0
            left_side = max(0,post_order(root.left))
            right_side = max(0,post_order(root.right))
            count[0]= max(count[0],left_side + right_side+root.val)
            return max(left_side, right_side)+root.val
            
        post_order(root)   
        return count[0]