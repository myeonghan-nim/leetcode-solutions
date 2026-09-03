class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        # 최솟값과 최댓값 사이의 정수 중 집합에 없는 것을 모두 모은다
        # 시간 복잡도: O(n + max - min)
        s = set(nums)
        return [x for x in range(min(s) + 1, max(s)) if x not in s]
