class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        # 루트에서 리프까지 내려가며 비트를 왼쪽으로 한 칸씩 밀어(2배) 이진수를 만들고, 리프에 도착하면 그 값을 더한다
        # 시간 복잡도: O(n)
        def sum_paths(node: Optional[TreeNode], number: int) -> int:
            if not node:
                return 0

            number = number * 2 + node.val  # 이진수 끝에 비트 하나를 붙이는 것과 같다
            if not (node.left or node.right):  # 리프
                return number

            return sum_paths(node.left, number) + sum_paths(node.right, number)
        return sum_paths(root, 0)
