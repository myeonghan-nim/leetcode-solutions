class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        # 짝수 인덱스끼리, 홀수 인덱스끼리만 교환할 수 있으므로 각 그룹을 정렬해 같은지 비교한다
        # 시간 복잡도: O(n log n)
        return sorted(s1[::2]) == sorted(s2[::2]) and sorted(s1[1::2]) == sorted(s2[1::2])
