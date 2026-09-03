class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        # 교환 가능한 인덱스끼리 유니온-파인드로 묶으면 같은 그룹 안에서는 자유롭게 재배치할 수 있다. 그룹별로 source와 target의 값 개수 차이를 세면 맞출 수 없는 위치 수가 나온다
        # 시간 복잡도: O(n·α(n))
        n = len(source)
        parent = list(range(n))
        size = [1] * n

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a: int, b: int) -> None:
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if size[ra] < size[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            size[ra] += size[rb]

        for a, b in allowedSwaps:
            union(a, b)

        delta = defaultdict(Counter)
        for i, (s, t) in enumerate(zip(source, target)):
            root = find(i)
            delta[root][s] += 1
            delta[root][t] -= 1  # 그룹 안에서 source에는 있고 target에는 없는 값의 개수가 양수로 남는다

        return sum(v for counter in delta.values() for v in counter.values() if v > 0)  # 양수만 더하면 짝을 못 찾는 위치 수
