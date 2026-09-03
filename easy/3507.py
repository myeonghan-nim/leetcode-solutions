class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        # 인접 쌍 중 합이 가장 작은 쌍을 합치는 연산을 배열이 비내림차순이 될 때까지 반복한다. 매번 전체를 재검사하지 않고, 합쳐지는 자리 주변 3쌍의 '내림 쌍' 수만 갱신한다
        # 시간 복잡도: O(n^2)
        bad = sum(nums[i] > nums[i + 1] for i in range(len(nums) - 1))  # 내림 쌍(nums[i] > nums[i+1])의 개수
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
