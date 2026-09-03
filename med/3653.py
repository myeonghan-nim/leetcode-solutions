class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        # 각 쿼리를 그대로 적용한 뒤 전체 XOR을 구한다
        # 시간 복잡도: O(q·n)
        MOD = 10**9 + 7
        for start, end, step, mult in queries:
            for i in range(start, end + 1, step):
                nums[i] = nums[i] * mult % MOD

        res = 0
        for num in nums:
            res ^= num

        return res
