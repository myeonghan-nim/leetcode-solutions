class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 짧은 배열을 이진 탐색해 두 배열을 '왼쪽 절반 / 오른쪽 절반'으로 나누는 분할점을 찾는다. 왼쪽의 최댓값 <= 오른쪽의 최솟값이면 그 경계가 중앙값이다
        # 시간 복잡도: O(log min(m, n))
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        left_size = (m + n + 1) // 2

        lo, hi = 0, m
        while True:
            i = (lo + hi) // 2
            j = left_size - i

            left1 = nums1[i - 1] if i > 0 else float("-inf")
            right1 = nums1[i] if i < m else float("inf")
            left2 = nums2[j - 1] if j > 0 else float("-inf")
            right2 = nums2[j] if j < n else float("inf")

            if left1 > right2:  # nums1에서 너무 많이 가져왔으니 i를 줄인다
                hi = i - 1
            elif left2 > right1:  # nums1에서 너무 적게 가져왔으니 i를 늘린다
                lo = i + 1
            else:
                if (m + n) % 2:
                    return float(max(left1, left2))
                return (max(left1, left2) + min(right1, right2)) / 2
