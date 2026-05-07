class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        t = "^#" + "#".join(s) + "#$"
        radius = [0] * len(t)

        center = 0
        right = 0
        best_center = 0
        best_radius = 0

        for i in range(1, len(t) - 1):
            mirror = 2 * center - i

            if i < right:
                radius[i] = min(right - i, radius[mirror])

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
