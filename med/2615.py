class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n

        count = {}
        sum_so_far = {}
        for i in range(n):
            num = nums[i]
            if num in count:
                ans[i] += count[num] * i - sum_so_far[num]
            count[num] = count.get(num, 0) + 1
            sum_so_far[num] = sum_so_far.get(num, 0) + i

        count.clear()
        sum_so_far.clear()
        for i in range(n - 1, -1, -1):
            num = nums[i]
            if num in count:
                ans[i] += sum_so_far[num] - count[num] * i
            count[num] = count.get(num, 0) + 1
            sum_so_far[num] = sum_so_far.get(num, 0) + i

        return ans
