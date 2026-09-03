from heapq import nsmallest


class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        # 첫 그룹은 반드시 nums[0]에서 시작하므로 nums[0]은 고정이고, 나머지에서 가장 작은 두 값을 고르면 된다
        # 시간 복잡도: O(n)
        return nums[0] + sum(nsmallest(2, nums[1:]))
