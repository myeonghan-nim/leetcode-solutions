class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 첫 문자열을 접두사 후보로 두고, 각 문자열이 그 후보로 시작할 때까지 후보를 뒤에서 한 글자씩 줄인다
        # 시간 복잡도: O(S) — S는 모든 문자열 길이의 합
        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""

        return prefix
