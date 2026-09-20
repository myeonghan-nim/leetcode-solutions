class Solution:
    def reverseDegree(self, s: str) -> int:
        # 각 문자의 역순 알파벳 값 (ord('z') - ord(c) + 1)에 1-indexed 위치를 곱해 더한다
        # 시간 복잡도: O(n)
        return sum((122 - ord(c) + 1) * i for i, c in enumerate(s, 1))
