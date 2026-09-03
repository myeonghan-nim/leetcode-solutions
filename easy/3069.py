class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        # 두 배열의 마지막 원소를 비교해 큰 쪽 배열에 다음 원소를 붙이는 규칙을 그대로 시뮬레이션하고, 끝나면 arr1 뒤에 arr2를 이어 붙인다
        # 시간 복잡도: O(n)
        arr1 = [nums[0]]
        arr2 = [nums[1]]

        for i in range(2, len(nums)):
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])

        arr1.extend(arr2)
        return arr1
