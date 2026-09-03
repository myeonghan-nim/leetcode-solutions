class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # 행 리스트를 만들고, 위아래로 방향을 바꾸며 문자를 해당 행에 넣은 뒤 행 순서대로 이어 붙인다
        # 시간 복잡도: O(n)
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [[] for _ in range(numRows)]
        index, step = 0, 1

        for char in s:
            rows[index].append(char)
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step

        return ''.join(''.join(row) for row in rows)
