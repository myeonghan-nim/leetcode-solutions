class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # 두 이진 문자열을 정수로 바꿔 더한 뒤 다시 이진 문자열로 포맷한다
        # 시간 복잡도: O(n)
        return f"{int(a, 2) + int(b, 2):b}"
