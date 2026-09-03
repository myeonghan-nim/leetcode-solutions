class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        # 홀수는 그대로 두고 짝수는 더 작은 홀수를 빼면 홀수가 된다. 따라서 최솟값이 홀수면 모두 홀수로 만들 수 있고, 최솟값이 짝수면 가장 작은 홀수를 짝수로 바꿀 방법이 없어 처음부터 모두 짝수여야 한다
        # 시간 복잡도: O(n)
        minimum = min(nums1)
        all_even = all(x % 2 == 0 for x in nums1)
        return minimum % 2 != 0 or all_even
