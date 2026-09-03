class Solution:
    def smallestSubsequence(self, s: str) -> str:
        # 단조 스택. 문자를 차례로 넣되, 스택 위 문자가 현재 문자보다 크고 뒤에 다시 나온다면 빼서 사전순을 낮춘다. 이미 스택에 있는 문자는 건너뛴다
        # 시간 복잡도: O(n)
        last = {c: i for i, c in enumerate(s)}
        stack, seen = [], set()
        for i, c in enumerate(s):
            if c in seen:
                continue
            while stack and stack[-1] > c and last[stack[-1]] > i:
                seen.remove(stack.pop())
            stack.append(c)
            seen.add(c)
        return ''.join(stack)
