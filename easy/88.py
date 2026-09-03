class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # 뒤에서부터 큰 값을 nums1의 끝자리에 채우면 덮어쓰기 없이 제자리에서 병합할 수 있다. nums1이 먼저 소진되면 남은 nums2는 그대로 채운다
        # 시간 복잡도: O(m + n)
        i, j, k = m - 1, n - 1, m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
