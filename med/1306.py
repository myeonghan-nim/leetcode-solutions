class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        # 각 위치에서 ±arr[i]로 갈 수 있는 인덱스를 간선으로 보고 DFS. 값이 0인 위치에 도달하면 성공
        # 시간 복잡도: O(n)
        n = len(arr)
        visited = {start}
        stack = [start]

        while stack:
            index = stack.pop()

            if arr[index] == 0:
                return True

            for next_index in (index + arr[index], index - arr[index]):
                if 0 <= next_index < n and next_index not in visited:
                    visited.add(next_index)
                    stack.append(next_index)

        return False
