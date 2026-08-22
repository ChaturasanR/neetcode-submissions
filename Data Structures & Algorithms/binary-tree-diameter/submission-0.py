# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    _diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        self._findMaxDiameter(root);
        return self._diameter

        

    def _findMaxDiameter(self, root: optional[TreeNode]) -> int:
        if root is None:
            return 0

        left_sub_tree_height = self._findMaxDiameter(root.left);
        right_sub_tree_height = self._findMaxDiameter(root.right);

        self._diameter = max(self._diameter, left_sub_tree_height + right_sub_tree_height)
        
        return max(left_sub_tree_height, right_sub_tree_height) + 1
        