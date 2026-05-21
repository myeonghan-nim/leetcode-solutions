class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
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
