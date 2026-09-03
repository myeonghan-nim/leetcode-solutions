class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # val이 아닌 원소만 앞쪽 k번째 자리에 차례로 옮겨 담는다
        # 시간 복잡도: O(n)
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
