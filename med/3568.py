from collections import deque
from typing import List


class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        # 상태를 (행, 열, 주운 쓰레기 비트마스크)로 두고 이동 횟수 순으로 BFS. 같은 상태를 더 많은 에너지로 다시 방문할 때만 확장해 가지치기한다
        # 시간 복잡도: O(m·n·2^L·(m·n)) 최악 — L은 쓰레기 수(최대 10)
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
                if e == 0:  # 에너지가 없으면 더 못 움직인다
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
                    elif cell == 'R':  # 충전 칸은 에너지를 가득 채운다
                        ne = energy
                    key = (nr, nc, nmask)
                    if best.get(key, -1) >= ne:  # 같은 상태를 더 많은(또는 같은) 에너지로 이미 왔다면 볼 필요 없다
                        continue
                    best[key] = ne
                    q.append((nr, nc, nmask, ne))
        return -1
