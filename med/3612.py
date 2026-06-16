from collections import deque


class Solution:
    def processStr(self, s: str) -> str:
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
