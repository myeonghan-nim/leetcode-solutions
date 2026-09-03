class Solution:
    def binaryGap(self, n: int) -> int:
        # 이진 문자열을 훑으며 직전 1의 위치를 기억하고, 새 1을 만날 때마다 거리를 갱신한다
        # 시간 복잡도: O(log n)
        distance, prev = 0, -1
        for idx, b in enumerate(bin(n)[2:]):
            if b == '1':
                if prev != -1:
                    distance = max(distance, idx - prev)
                prev = idx
        return distance
