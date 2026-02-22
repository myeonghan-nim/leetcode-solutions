class Solution:
    def binaryGap(self, n: int) -> int:
        distance, prev = 0, -1
        for idx, b in enumerate(bin(n)[2:]):
            if b == '1':
                if prev != -1:
                    distance = max(distance, (idx - prev))
                prev = idx
        return distance
