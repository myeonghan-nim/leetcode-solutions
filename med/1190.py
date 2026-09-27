class Solution:
    def reverseParentheses(self, s: str) -> str:
        # 괄호 쌍을 미리 짝지어 두고, 괄호를 만나면 짝 위치로 순간이동하며 진행 방향을 뒤집어 문자열을 한 번만 훑는다 (웜홀 기법)
        # 시간 복잡도: O(n)
        n = len(s)
        pair = [0] * n
        stack = []
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                j = stack.pop()
                pair[i], pair[j] = j, i

        result = []
        i, step = 0, 1
        while i < n:
            if s[i] in '()':
                i = pair[i]  # 짝으로 점프한 뒤 반대 방향으로 진행하면 괄호 안을 뒤집어 읽는 효과
                step = -step
            else:
                result.append(s[i])
            i += step
        return ''.join(result)
