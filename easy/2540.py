class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        # 두 배열 모두 정렬되어 있으므로 포인터 두 개를 앞에서부터 움직이며 작은 쪽을 전진시킨다
        # 시간 복잡도: O(m + n)
        i, j = 0, 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                return nums1[i]
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

        return -1
