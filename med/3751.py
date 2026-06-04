class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        count = 0

        for n in range(num1, num2 + 1):
            s = str(n)
            if len(s) < 2:
                continue

            for i in range(1, len(s) - 1):
                if (s[i] > s[i - 1] and s[i] > s[i + 1]) or (s[i] < s[i - 1] and s[i] < s[i + 1]):
                    count += 1

        return count
