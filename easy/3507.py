class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        bad = sum(nums[i] > nums[i + 1] for i in range(len(nums) - 1))
        ops = 0

        while bad > 0:
            min_idx = min(range(len(nums) - 1), key=lambda i: nums[i] + nums[i + 1])

            if min_idx > 0 and nums[min_idx - 1] > nums[min_idx]:
                bad -= 1
            if nums[min_idx] > nums[min_idx + 1]:
                bad -= 1
            if min_idx + 2 < len(nums) and nums[min_idx + 1] > nums[min_idx + 2]:
                bad -= 1

            nums[min_idx:min_idx + 2] = [nums[min_idx] + nums[min_idx + 1]]

            if min_idx > 0 and nums[min_idx - 1] > nums[min_idx]:
                bad += 1
            if min_idx < len(nums) - 1 and nums[min_idx] > nums[min_idx + 1]:
                bad += 1

            ops += 1

        return ops
