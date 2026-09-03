class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        # 소문자 c에 대해 대문자 C도 있으면 특수 문자. 집합에 넣어 두고 확인한다
        # 시간 복잡도: O(n)
        chars = set(word)
        return sum(1 for char in chars if char.islower() and char.upper() in chars)
