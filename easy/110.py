class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height_or_unbalanced(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            left_height = height_or_unbalanced(node.left)
            if left_height == -1:
                return -1
            right_height = height_or_unbalanced(node.right)
            if right_height == -1:
                return -1
            if abs(left_height - right_height) > 1:
                return -1
            return max(left_height, right_height) + 1
        return height_or_unbalanced(root) != -1
