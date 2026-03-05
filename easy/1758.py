class Solution:
    def minOperations(self, s: str) -> int:
        mismatch_start_with_0 = s[::2].count("1") + s[1::2].count("0")
        return min(mismatch_start_with_0, len(s) - mismatch_start_with_0)
