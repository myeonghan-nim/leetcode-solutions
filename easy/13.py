class Solution:
    def romanToInt(self, s: str) -> int:
        # 뒤에서부터 읽으면서 현재 값이 직전(오른쪽) 값보다 작으면 뺄셈 표기(IV, IX 등)이므로 빼고, 아니면 더한다
        # 시간 복잡도: O(n)
        roman_numerals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        prev_value = total = 0
        for char in reversed(s):
            current_value = roman_numerals[char]
            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value
            prev_value = current_value

        return total
