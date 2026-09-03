from collections import deque


class Solution:
    def processStr(self, s: str) -> str:
        # 뒤집기(%)를 실제로 수행하지 않고 '뒤집힌 상태' 플래그만 유지한다. 뒤집힌 상태에서는 앞쪽에 추가/삭제하는 것이 원래 순서의 뒤쪽 작업과 같으므로 덱을 쓴다
        # 시간 복잡도: O(n^2) 최악 — '#'가 문자열을 통째로 복제
        result = deque()
        reversed_order = False

        for c in s:
            if c == '#':
                result.extend(list(result))
            elif c == '%':
                reversed_order = not reversed_order
            elif c == '*':
                if result:
                    if reversed_order:
                        result.popleft()
                    else:
                        result.pop()
            else:
                if reversed_order:
                    result.appendleft(c)
                else:
                    result.append(c)

        return ''.join(reversed(result)) if reversed_order else ''.join(result)
