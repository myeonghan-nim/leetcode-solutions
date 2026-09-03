class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 중위 순회 = 왼쪽 서브트리 → 자기 자신 → 오른쪽 서브트리. 재귀 결과를 리스트로 이어 붙인다
        # 시간 복잡도: O(n·h) — 리스트 이어 붙이기 비용, h는 트리 높이
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
