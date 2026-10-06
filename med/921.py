class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_ = need = 0
        for c in s:
            if c == "(":
                open_ += 1
            elif open_:
                open_ -= 1
            else:
                need += 1
        return open_ + need
