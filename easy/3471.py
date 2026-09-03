from collections import Counter


class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        # 길이 k인 부분 배열 전체에서 정확히 한 번 나타나는 최댓값. k == n이면 전체 max, k == 1이면 배열에서 한 번만 나오는 값, 그 외에는 오직 양 끝 원소만 한 부분 배열에만 속한다
        # 시간 복잡도: O(n)
        n, count = len(nums), Counter(nums)
        if k == n:
            return max(nums)

        candidates = nums if k == 1 else (nums[0], nums[-1])
        return max((x for x in candidates if count[x] == 1), default=-1)
