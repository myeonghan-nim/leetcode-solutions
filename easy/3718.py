class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        # k, 2k, 3k, ... 순서로 올라가며 배열에 없는 첫 번째 배수를 찾는다
        # 시간 복잡도: O(n + answer / k)
        seen = set(nums)
        multiple = k
        while multiple in seen:
            multiple += k
        return multiple
