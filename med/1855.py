class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        # 두 배열 모두 비증가이므로 투 포인터. nums1[i] <= nums2[j]면 유효한 쌍이니 j를 늘려 거리를 키우고, 아니면 i를 늘린다
        # 시간 복잡도: O(m + n)
        i = j = ans = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                ans = max(ans, j - i)
                j += 1
            else:
                i += 1
                if i > j:
                    j = i
        return ans
