class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        chars = set(word)
        return sum(1 for char in chars if char.islower() and char.upper() in chars)
