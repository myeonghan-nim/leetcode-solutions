class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        # 구간 합이 홀수라는 것은 양 끝 누적 합의 홀짝이 다르다는 뜻이므로, 홀수 누적 합 개수 × 짝수 누적 합 개수가 답이다
        # 시간 복잡도: O(n)
        parity = odd_count = 0
        for num in arr:
            parity ^= num & 1
            odd_count += parity
        even_count = len(arr) + 1 - odd_count  # 빈 접두사(합 0)도 짝수 누적 합에 포함한다
        return odd_count * even_count % (10**9 + 7)
