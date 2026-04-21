class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
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
            delta[root][t] -= 1

        return sum(v for counter in delta.values() for v in counter.values() if v > 0)
