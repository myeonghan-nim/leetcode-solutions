class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        # 후위 순회로 각 서브트리의 (합, 노드 수)를 자식에서 부모로 올려 보내며, 합 // 노드 수가 현재 노드 값과 같으면 센다
        # 시간 복잡도: O(n)
        count = 0

        def dfs(node: TreeNode) -> tuple[int, int]:
            nonlocal count
            if not node:
                return 0, 0

            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)
            total = left_sum + right_sum + node.val
            size = left_count + right_count + 1
            if total // size == node.val:
                count += 1

            return total, size

        dfs(root)
        return count
