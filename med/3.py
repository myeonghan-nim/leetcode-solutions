class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 슬라이딩 윈도우. 각 문자의 마지막 위치를 기억해 두고, 창 안에서 중복이 생기면 left를 그 위치 다음으로 옮긴다
        # 시간 복잡도: O(n)
        left = 0
        char_index_map = {}
        max_length = 0

        for right in range(len(s)):
            if s[right] in char_index_map and char_index_map[s[right]] >= left:
                left = char_index_map[s[right]] + 1

            char_index_map[s[right]] = right
            max_length = max(max_length, right - left + 1)

        return max_length
