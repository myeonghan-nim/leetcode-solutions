class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # 앞에서부터 1씩 커지는 가장 긴 접두사의 합을 구한 뒤, 그 합부터 시작해 배열에 없는 가장 작은 수를 찾는다
        # 시간 복잡도: O(n)
        total = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                break
            total += nums[i]

        seen = set(nums)
        while total in seen:
            total += 1
        return total
