class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        # 첫 행을 전부 비우고 나머지 행은 마지막 열만 비우면 "오른쪽 끝까지 간 뒤 아래로"가 유일한 경로가 된다
        # 시간 복잡도: O(m * n)
        return ["." * n] + ["#" * (n - 1) + "."] * (m - 1)
