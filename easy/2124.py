class Solution:
    def checkString(self, s: str) -> bool:
        # 어떤 'a'가 'b'보다 뒤에 있으면 그 사이 어딘가에 반드시 'b' 바로 다음 'a'가 붙어 있으므로, 'ba'가 없는지만 확인하면 된다
        # 시간 복잡도: O(n)
        return 'ba' not in s
