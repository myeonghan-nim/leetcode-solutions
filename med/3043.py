class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        # arr1의 모든 수에서 나올 수 있는 접두사(10으로 나눠 가며)를 집합에 담고, arr2의 각 수도 접두사를 줄여 가며 집합에 있는 가장 긴 길이를 찾는다
        # 시간 복잡도: O((n + m) · log M)
        prefixes = set()
        for num in arr1:
            while num:
                prefixes.add(num)
                num //= 10

        longest_prefix = 0
        for num in arr2:
            length = len(str(num))
            while num and length > longest_prefix:
                if num in prefixes:
                    longest_prefix = length
                    break
                num //= 10
                length -= 1

        return longest_prefix
