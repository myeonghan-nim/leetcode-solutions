from heapq import nlargest, nsmallest


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # 세 수의 곱이 최대인 경우는 '가장 큰 세 수' 또는 '가장 작은 두 음수 × 가장 큰 수' 둘 중 하나이다
        # 시간 복잡도: O(n)
        top3 = nlargest(3, nums)
        low2 = nsmallest(2, nums)
        return max(top3[0] * top3[1] * top3[2], top3[0] * low2[0] * low2[1])
