class Solution:
    def maxDistinct(self, s: str) -> int:
        # 서로 다른 문자의 개수가 답이다
        # 시간 복잡도: O(n)
        return len(set(s))
