class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        # 1-indexed 위치 i가 n의 약수인 원소만 골라 제곱해 더하며, 배열 인덱스는 0-indexed이므로 nums[i - 1]을 쓴다
        # 시간 복잡도: O(n)
        n = len(nums)
        return sum(nums[i - 1] ** 2 for i in range(1, n + 1) if n % i == 0)
