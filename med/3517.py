class Solution:
    def smallestPalindrome(self, s: str) -> str:
        # 문자별 개수를 절반씩 사전순으로 나열해 앞 절반을 만들고, 홀수 개인 문자를 가운데, 앞 절반을 뒤집어 뒤에 붙인다
        # 시간 복잡도: O(n)
        cnt = Counter(s)
        half = "".join(ch * (n // 2) for ch, n in sorted(cnt.items()))
        mid = next((ch for ch, n in cnt.items() if n % 2), "")
        return half + mid + half[::-1]
