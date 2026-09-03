class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # 각 행은 내림차순이므로 뒤에서부터 음수를 세다가 0 이상을 만나면 그 행은 멈춘다
        # 시간 복잡도: O(m·n) 최악 — 전부 음수인 경우
        count = 0
        for row in grid:
            for c in row[::-1]:
                if c < 0:
                    count += 1
                else:
                    break
        return count
