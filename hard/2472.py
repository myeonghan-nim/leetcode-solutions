class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n, count, end = len(s), 0, -1
        for i in range(n):
            for lo, hi in ((i, i + k - 1), (i, i + k)):
                if hi >= n or lo <= end:
                    continue
                if all(s[lo + j] == s[hi - j] for j in range((hi - lo + 1) // 2)):
                    count += 1
                    end = hi
                    break
        return count
