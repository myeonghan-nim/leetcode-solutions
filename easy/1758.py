class Solution:
    def minOperations(self, s: str) -> int:
        # 목표 패턴은 "0101..." 또는 "1010..." 둘뿐. 짝수 자리의 '1' 개수 + 홀수 자리의 '0' 개수가 첫 패턴과 다른 자리 수이고, 다른 패턴은 그 여집합이다
        # 시간 복잡도: O(n)
        mismatch_start_with_0 = s[::2].count("1") + s[1::2].count("0")
        return min(mismatch_start_with_0, len(s) - mismatch_start_with_0)
