class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        # nums가 1..n의 순열이므로 n이 1, 2면 nums 자체만 가능하고, 3 이상이면 n의 비트 길이 안의 모든 값을 XOR로 만들 수 있다
        # 시간 복잡도: O(1)
        n = len(nums)
        return n if n <= 2 else 1 << n.bit_length()
