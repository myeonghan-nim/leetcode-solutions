class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        # 범위 안의 모든 수에 대해 가운데 자릿수가 양옆보다 모두 크거나 모두 작은 위치를 센다
        # 시간 복잡도: O((num2 - num1) · log num2)
        count = 0

        for n in range(num1, num2 + 1):
            s = str(n)
            if len(s) < 2:
                continue

            for i in range(1, len(s) - 1):
                if (s[i] > s[i - 1] and s[i] > s[i + 1]) or (s[i] < s[i - 1] and s[i] < s[i + 1]):
                    count += 1

        return count
