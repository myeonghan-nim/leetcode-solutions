class Solution:
    def isGood(self, nums: List[int]) -> bool:
        # 길이가 n+1이면 base[n]은 1..n-1이 한 번씩, n이 두 번 나와야 한다. 개수 배열로 세어 확인한다
        # 시간 복잡도: O(n)
        n = len(nums) - 1
        if n < 1:
            return False

        count = [0] * (n + 1)

        for num in nums:
            if num < 1 or num > n:
                return False
            count[num] += 1

        for value in range(1, n):
            if count[value] != 1:
                return False

        return count[n] == 2
