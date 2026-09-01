from collections import deque
from typing import List


class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        litter = {}
        for i in range(m):
            for j in range(n):
                c = classroom[i][j]
                if c == 'S':
                    sr, sc = i, j
                elif c == 'L':
                    litter[(i, j)] = len(litter)

        full = (1 << len(litter)) - 1
        if full == 0:
            return 0

        best = {(sr, sc, 0): energy}
        q = deque([(sr, sc, 0, energy)])
        moves = 0
        while q:
            moves += 1
            for _ in range(len(q)):
                r, c, mask, e = q.popleft()
                if e == 0:
                    continue
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if not (0 <= nr < m and 0 <= nc < n):
                        continue
                    cell = classroom[nr][nc]
                    if cell == 'X':
                        continue
                    ne = e - 1
                    nmask = mask
                    if cell == 'L':
                        nmask |= 1 << litter[(nr, nc)]
                        if nmask == full:
                            return moves
                    elif cell == 'R':
                        ne = energy
                    key = (nr, nc, nmask)
                    if best.get(key, -1) >= ne:
                        continue
                    best[key] = ne
                    q.append((nr, nc, nmask, ne))
        return -1
