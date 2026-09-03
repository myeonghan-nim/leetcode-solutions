class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        # nums가 정렬되어 있으므로 인접 차이가 maxDiff를 넘는 곳에서 그룹이 끊긴다. 각 인덱스의 그룹 번호를 누적으로 매기고 같은 그룹인지 비교한다
        # 시간 복잡도: O(n + q)
        comp = [0] * n
        for i in range(1, n):
            comp[i] = comp[i - 1] + (nums[i] - nums[i - 1] > maxDiff)
        return [comp[u] == comp[v] for u, v in queries]
