class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 이진 탐색. 못 찾으면 left가 target이 들어갈 자리(target보다 큰 첫 위치)를 가리킨다
        # 시간 복잡도: O(log n)
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left
