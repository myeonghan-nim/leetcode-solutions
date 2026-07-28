class Solution:
    def smallestPalindrome(self, s: str) -> str:
        cnt = Counter(s)
        half = "".join(ch * (n // 2) for ch, n in sorted(cnt.items()))
        mid = next((ch for ch, n in cnt.items() if n % 2), "")
        return half + mid + half[::-1]
