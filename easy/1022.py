class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def sumNodes(node: Optional[TreeNode], number: int) -> int:
            if not node:
                return 0

            number = number * 2 + node.val
            if not (node.left or node.right):
                return number

            return sumNodes(node.left, number) + sumNodes(node.right, number)
        return sumNodes(root, 0)
