class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # split()은 앞뒤 공백을 무시하고 단어만 나누므로 마지막 원소가 마지막 단어이다
        # 시간 복잡도: O(n)
        return len(s.split()[-1])
