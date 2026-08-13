class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        arr = list(s)
        pref = [0] * (4 * n)
        suf = [0] * (4 * n)
        best = [0] * (4 * n)

        def pull(node: int, l: int, m: int, r: int) -> None:
            lc, rc = 2 * node, 2 * node + 1
            left_len, right_len = m - l + 1, r - m
            pref[node] = pref[lc]
            suf[node] = suf[rc]
            best[node] = max(best[lc], best[rc])
            if arr[m] == arr[m + 1]:
                best[node] = max(best[node], suf[lc] + pref[rc])
                if pref[lc] == left_len:
                    pref[node] = left_len + pref[rc]
                if suf[rc] == right_len:
                    suf[node] = right_len + suf[lc]

        def build(node: int, l: int, r: int) -> None:
            if l == r:
                pref[node] = suf[node] = best[node] = 1
                return
            m = (l + r) // 2
            build(2 * node, l, m)
            build(2 * node + 1, m + 1, r)
            pull(node, l, m, r)

        def update(node: int, l: int, r: int, i: int) -> None:
            if l == r:
                return
            m = (l + r) // 2
            if i <= m:
                update(2 * node, l, m, i)
            else:
                update(2 * node + 1, m + 1, r, i)
            pull(node, l, m, r)

        build(1, 0, n - 1)
        ans = []
        for c, i in zip(queryCharacters, queryIndices):
            arr[i] = c
            update(1, 0, n - 1, i)
            ans.append(best[1])
        return ans
