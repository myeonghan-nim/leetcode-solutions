class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        # 정렬하면 차이가 최소인 k개는 반드시 연속 구간이므로, 길이 k 창을 밀며 양 끝 차이의 최솟값을 구한다
        # 시간 복잡도: O(n log n)
        nums.sort()
        return min(nums[i + k - 1] - nums[i] for i in range(len(nums) - k + 1))
