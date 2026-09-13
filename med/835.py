class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        # 두 이미지의 1 좌표 쌍마다 이동 벡터(dx, dy)를 세어, 가장 많이 등장한 벡터의 빈도가 곧 그 이동으로 겹치는 1의 개수다
        # 시간 복잡도: O(A * B) (A, B는 각 이미지의 1의 개수, 최악 O(n^4))
        n = len(img1)
        ones1 = [(r, c) for r in range(n) for c in range(n) if img1[r][c]]
        ones2 = [(r, c) for r in range(n) for c in range(n) if img2[r][c]]

        counter = Counter((r1 - r2, c1 - c2) for r1, c1 in ones1 for r2, c2 in ones2)
        return max(counter.values(), default=0)  # 1이 하나도 없는 이미지는 겹침 0
