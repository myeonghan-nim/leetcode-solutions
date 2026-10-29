class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        # 루트→x 경로의 문자 비트 XOR(pre)을 오일러 투어 + 펜윅 트리로 관리하고, u-v 경로 마스크는 pre[u]^pre[v]^bit(lca)로 복원해 홀수 개 문자가 1종 이하인지 확인
        # 시간 복잡도: O((n + q) log n)
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        parent, depth, order, stack = [0] * n, [0] * n, [], [0]
        while stack:
            u = stack.pop()
            order.append(u)
            for v in adj[u]:
                if v != parent[u]:
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    stack.append(v)

        size, tin = [1] * n, [0] * n
        for u in reversed(order[1:]):
            size[parent[u]] += size[u]
        for i, u in enumerate(order):
            tin[u] = i

        up = [parent]  # up[k][v] = v의 2^k번째 조상(이진 리프팅)
        for _ in range(max(depth).bit_length() - 1):
            prev = up[-1]
            up.append([prev[prev[v]] for v in range(n)])

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            diff, k = depth[u] - depth[v], 0
            while diff:
                if diff & 1:
                    u = up[k][u]
                diff >>= 1
                k += 1
            if u == v:
                return u
            for jump in reversed(up):
                if jump[u] != jump[v]:
                    u, v = jump[u], jump[v]
            return parent[u]

        tree = [0] * (n + 1)  # 차분 배열 위 펜윅 트리: 접두 XOR이 곧 pre[x]

        def update(i, bit):
            while i <= n:
                tree[i] ^= bit
                i += i & -i

        def prefix(i):
            acc = 0
            while i:
                acc ^= tree[i]
                i -= i & -i
            return acc

        def flip_subtree(u, bit):  # s[u]가 바뀌면 u의 서브트리 전체 pre에 bit가 XOR됨
            update(tin[u] + 1, bit)
            update(tin[u] + size[u] + 1, bit)

        code = [ord(c) - 97 for c in s]
        for u in range(n):
            flip_subtree(u, 1 << code[u])

        answer = []
        for q in queries:
            op, a, b = q.split()
            a = int(a)
            if op == 'update':
                c = ord(b) - 97
                flip_subtree(a, (1 << code[a]) ^ (1 << c))
                code[a] = c
            else:
                b = int(b)
                mask = prefix(tin[a] + 1) ^ prefix(tin[b] + 1) ^ (1 << code[lca(a, b)])  # pre[a]^pre[b]는 lca를 두 번 지워 한 번 되살림
                answer.append(mask & (mask - 1) == 0)
        return answer
