class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 읽기 포인터로 훑으며 직전 값과 다른 원소만 쓰기 포인터 자리에 옮겨 담는다(정렬되어 있어 중복은 항상 인접)
        # 시간 복잡도: O(n)
        write_index = 1
        for read_index in range(1, len(nums)):
            if nums[read_index] != nums[read_index - 1]:
                nums[write_index] = nums[read_index]
                write_index += 1

        return write_index
