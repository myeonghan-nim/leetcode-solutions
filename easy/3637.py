class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        # 앞에서 증가가 끝나는 지점 p, 뒤에서 증가가 시작되는 지점 q를 찾고, 0 < p < q < n-1 이면서 p..q 구간이 엄격히 감소하는지 확인한다
        # 시간 복잡도: O(n)
        n = len(nums)

        p = 0
        while p < n - 1 and nums[p] < nums[p + 1]:
            p += 1

        q = n - 1
        while q > 0 and nums[q - 1] < nums[q]:
            q -= 1

        return 0 < p < q < n - 1 and all(nums[i] > nums[i + 1] for i in range(p, q))
