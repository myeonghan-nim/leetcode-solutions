class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 가능한 모든 시작 위치에서 needle 길이만큼 잘라 비교한다
        # 시간 복잡도: O(n·m)
        if not needle:
            return 0

        needle_length = len(needle)
        for i in range(len(haystack) - needle_length + 1):
            if haystack[i:i + needle_length] == needle:
                return i

        return -1
