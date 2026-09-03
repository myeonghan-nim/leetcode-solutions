class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        arr = list(s)
        pref = [0] * (4 * n)
        suf = [0] * (4 * n)
        best = [0] * (4 * n)

        def pull(node: int, lo: int, mid: int, hi: int) -> None:
            lc, rc = 2 * node, 2 * node + 1
            left_len, right_len = mid - lo + 1, hi - mid
            pref[node] = pref[lc]
            suf[node] = suf[rc]
            best[node] = max(best[lc], best[rc])
            if arr[mid] == arr[mid + 1]:
                best[node] = max(best[node], suf[lc] + pref[rc])
                if pref[lc] == left_len:
                    pref[node] = left_len + pref[rc]
                if suf[rc] == right_len:
                    suf[node] = right_len + suf[lc]

        def build(node: int, lo: int, hi: int) -> None:
            if lo == hi:
                pref[node] = suf[node] = best[node] = 1
                return
            mid = (lo + hi) // 2
            build(2 * node, lo, mid)
            build(2 * node + 1, mid + 1, hi)
            pull(node, lo, mid, hi)

        def update(node: int, lo: int, hi: int, i: int) -> None:
            if lo == hi:
                return
            mid = (lo + hi) // 2
            if i <= mid:
                update(2 * node, lo, mid, i)
            else:
                update(2 * node + 1, mid + 1, hi, i)
            pull(node, lo, mid, hi)

        build(1, 0, n - 1)
        ans = []
        for c, i in zip(queryCharacters, queryIndices):
            arr[i] = c
            update(1, 0, n - 1, i)
            ans.append(best[1])
        return ans
