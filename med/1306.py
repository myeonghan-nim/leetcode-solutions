class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
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
