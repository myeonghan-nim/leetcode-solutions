class Solution:
    def checkValidString(self, s: str) -> bool:
        # '*'의 선택에 따라 가능한 "열린 괄호 수"의 범위 [lo, hi]만 추적하면 되며, hi가 음수가 되면 실패, 끝에서 lo가 0이면 성공이다
        # 시간 복잡도: O(n)
        lo = hi = 0
        for c in s:
            if c == '(':
                lo += 1
                hi += 1
            elif c == ')':
                lo -= 1
                hi -= 1
            else:
                lo -= 1  # '*'를 ')'로 쓰면 최소값, '('로 쓰면 최대값이 각각 바뀐다
                hi += 1
            if hi < 0:
                return False
            lo = max(lo, 0)  # 열린 괄호 수가 음수인 경로는 이미 무효이므로 범위에서 잘라낸다
        return lo == 0
