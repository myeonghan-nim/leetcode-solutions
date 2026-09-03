class Solution:
    def isValid(self, s: str) -> bool:
        # 여는 괄호는 스택에 쌓고, 닫는 괄호가 나오면 스택 맨 위가 짝이 맞는 여는 괄호인지 확인한다
        # 시간 복잡도: O(n)
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else "#"  # 스택이 비면 짝 없는 닫는 괄호이므로 불일치 표식
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)

        return not stack  # 남은 여는 괄호가 없어야 유효
