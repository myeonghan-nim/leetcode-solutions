class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # 슬라이딩 윈도우. [left, right]가 a, b, c를 모두 포함하면 right 이후를 어디까지 늘려도 조건을 만족하므로 len(s) - right개를 한 번에 세고 left를 줄인다
        # 시간 복잡도: O(n)
        count = 0
        left = 0
        freq = {'a': 0, 'b': 0, 'c': 0}

        for right in range(len(s)):
            freq[s[right]] += 1

            while all(freq[char] > 0 for char in 'abc'):
                count += len(s) - right
                freq[s[left]] -= 1
                left += 1

        return count
