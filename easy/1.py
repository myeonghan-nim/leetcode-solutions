class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 지금까지 본 숫자와 그 위치를 딕셔너리에 기록하면서, target에서 현재 숫자를 뺀 값(짝)이 이미 기록돼 있는지 확인한다
        # 시간 복잡도: O(n)
        num_to_index = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], index]
            num_to_index[num] = index
        return []
