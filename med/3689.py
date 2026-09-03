class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        # 부분 배열 값 = max - min이고 전체 배열이 가장 크므로, 같은 전체 배열을 k번 고르면 최대
        # 시간 복잡도: O(n)
        return (max(nums) - min(nums)) * k
