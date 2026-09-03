class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # 고도 변화를 누적하면서 지나온 최고 고도를 기록한다. 출발 고도 0도 후보에 포함된다
        # 시간 복잡도: O(n)
        altitude = 0
        highest = 0

        for g in gain:
            altitude += g
            highest = max(highest, altitude)

        return highest
