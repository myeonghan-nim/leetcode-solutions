class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        ans = 0
        cur = 0
        less = 0
        freq = {0: 1}

        for x in nums:
            if x == target:
                less += freq.get(cur, 0)
                cur += 1
            else:
                less -= freq.get(cur - 1, 0)
                cur -= 1

            ans += less
            freq[cur] = freq.get(cur, 0) + 1

        return ans
