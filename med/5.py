class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Manacher 알고리즘. 문자 사이에 '#'를 끼워 홀짝 길이를 통일하고, 이미 알아낸 회문 범위 안에서는 대칭 위치의 반지름을 재활용한다
        # 시간 복잡도: O(n)
        t = "^#" + "#".join(s) + "#$"
        radius = [0] * len(t)

        center = 0
        right = 0
        best_center = 0
        best_radius = 0

        for i in range(1, len(t) - 1):
            mirror = 2 * center - i

            if i < right:
                radius[i] = min(right - i, radius[mirror])  # 오른쪽 경계까지의 거리와 거울 위치의 반지름 중 작은 값부터 시작

            while t[i + radius[i] + 1] == t[i - radius[i] - 1]:
                radius[i] += 1

            if i + radius[i] > right:
                center = i
                right = i + radius[i]

            if radius[i] > best_radius:
                best_center = i
                best_radius = radius[i]

        start = (best_center - best_radius) // 2
        return s[start:start + best_radius]
