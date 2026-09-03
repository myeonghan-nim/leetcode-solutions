class Solution:
    def minimumPushes(self, word: str) -> int:
        # 8개 키에 문자를 고르게 배정하면 i번째(0부터) 문자는 i // 8 + 1번 눌러야 한다
        # 시간 복잡도: O(n)
        return sum(i // 8 + 1 for i in range(len(word)))
