class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def sum_paths(node: Optional[TreeNode], number: int) -> int:
            if not node:
                return 0

            number = number * 2 + node.val
            if not (node.left or node.right):
                return number

            return sum_paths(node.left, number) + sum_paths(node.right, number)
        return sum_paths(root, 0)
