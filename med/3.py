class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        left = 0
        char_index_map = {}
        max_length = 1

        for right in range(len(s)):
            if s[right] in char_index_map and char_index_map[s[right]] >= left:
                left = char_index_map[s[right]] + 1

            char_index_map[s[right]] = right
            max_length = max(max_length, right - left + 1)

        return max_length
