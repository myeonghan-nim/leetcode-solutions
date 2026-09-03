class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # 중복을 제거해 정렬하면 순위 순서가 나온다. 값 -> 순위 딕셔너리를 만들어 각 원소를 치환한다
        # 시간 복잡도: O(n log n)
        rank = {v: i + 1 for i, v in enumerate(sorted(set(arr)))}
        return [rank[v] for v in arr]
